from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from app.models.certificate import Certificate
from app.serialization.serializers import CertificateSerializer


class CertificateView(generics.CreateAPIView, generics.RetrieveUpdateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CertificateActivateView(APIView):
    def post(self, request, pk, active=True, notify=False):
        # TODO: notify
        c = get_object_or_404(Certificate, pk=pk)
        serializer = CertificateSerializer(c, data={active: active})
        return Response(serializer.data)
