import asyncio
import logging
import requests

from rest_framework import generics, status
from django.conf import settings

from app.models.certificate import Certificate
from app.serialization.serializers import CertificateSerializer, \
    CertificateUpdateSerializer
from app.services import authority


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
                authority.update_authority(active=new_active, pk=pk,
                                           body=body))
            loop.close()

        return response
