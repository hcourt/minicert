import asyncio
import logging
import requests

from rest_framework import generics, status
from django.conf import settings

from app.models.certificate import Certificate
from app.serialization.serializers import CertificateSerializer, \
    CertificateUpdateSerializer


class CertificateView(generics.CreateAPIView, generics.RetrieveAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CertificateListView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CertificateActivateView(generics.UpdateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateUpdateSerializer

    def update(self, request, *args, **kwargs):
        """
        Wraps the superclass update method to additionally update a certificate
        authority when 'active' changes.

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        instance = self.get_object()
        old_active = getattr(instance, 'active', None)
        response = super().update(request, *args, **kwargs)

        if response.status_code != status.HTTP_200_OK:
            return response

        new_active = bool(request.data.get('active'))
        body = getattr(instance, 'cert_body', None)
        pk = getattr(instance, 'pk', None)

        if old_active != new_active:
            logging.debug(
                "Updating authority for certificate %s since active was "
                "changed.",
                pk)
            loop = asyncio.new_event_loop()
            loop.run_until_complete(
                self.update_authority(active=new_active, pk=pk,
                                      body=body))
            loop.close()

        return response

    @staticmethod
    async def update_authority(active=None, pk=None, body=None):
        """
        Asynchronously update a certificate authority on the active or inactive
        status of a certificate.

        :param active: True if the certificate has become active, False if
        the certificate has become inactive.
        :param pk: primary key of the certificate
        :param body: body of the certificate.  Will be sent to the authority.
        :return: after awaiting the post
        """

        async def _post_async(*args, **kwargs):
            return requests.post(*args, **kwargs)

        data = {'certificate': body, 'active': active}
        authority = settings.ACTIVATE_AUTHORITY

        loop = asyncio.get_event_loop()
        asyncio.set_event_loop(loop)
        task = loop.create_task(_post_async(authority, data))
        response = await task

        if response.status_code == status.HTTP_200_OK:
            logging.info(
                "Notified authority %s that certificate %s is %s",
                authority, pk, "active" if active else "inactive")
        else:
            logging.error(
                "Unable to notify authority %s that certificate %s is %s: "
                "status %s",
                authority, pk, "active" if active else "inactive",
                response.status_code)
        return
