from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models.certificate import Certificate
from app.serialization.serializers import CertificateSerializer


class CertificateView(APIView):
    def get(self, request, certificate_id):
        c = get_object_or_404(Certificate, pk=certificate_id)
        return Response(CertificateSerializer(c).data)

    def post(self, request, certificate_id):
        data = JSONParser().parse(request)
        serializer = CertificateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, certificate_id):
        c = get_object_or_404(Certificate, pk=certificate_id)
        data = JSONParser().parse(request)
        serializer = CertificateSerializer(instance=c, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CertificateActivateView(APIView):
    def post(self, request, certificate_id, active=True, notify=False):
        # TODO: notify
        c = get_object_or_404(Certificate, pk=certificate_id)
        return Response(CertificateSerializer(c).data)
