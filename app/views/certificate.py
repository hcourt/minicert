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
    # TODO: notify
    queryset = Certificate.objects.all()
    serializer_class = CertificateUpdateSerializer

    def update(self, request, *args, **kwargs):
        response = super().update(request, args, kwargs)

        if response.status_code == status.HTTP_200_OK:
            self._update_authority(kwargs.get("active"))

        return response

    @staticmethod
    def _update_authority(active):
        if active:
            # Call to Activate
            pass
        else:
            # Call to Deactivate
            pass
        return
