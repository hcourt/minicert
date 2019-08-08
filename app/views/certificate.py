from rest_framework import generics

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
