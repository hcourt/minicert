from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models.customer import Customer
from app.serialization.serializers import CustomerSerializer, \
    CertificateSerializer


class CustomerView(APIView):
    def get(self, request, customer_id):
        c = get_object_or_404(Customer, pk=customer_id)
        return Response(CustomerSerializer(c).data)

    def post(self, request, customer_id):
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, customer_id):
        c = get_object_or_404(Customer, pk=customer_id)
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(instance=c, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, customer_id):
        c = get_object_or_404(Customer, pk=customer_id)
        c.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class CustomerCertificatesView(APIView):
    def get(self, request, customer_id):
        c = get_object_or_404(Customer, pk=customer_id)
        certs = c.certificate_set.all()
        serialized_certs = {
            'results': CertificateSerializer(certs, many=True).data}
        return Response(serialized_certs)


class CustomerActiveCertificatesView(APIView):
    def get(self, request, customer_id):
        c = get_object_or_404(Customer, pk=customer_id)
        certs = c.certificate_set.filter(active=True)
        serialized_certs = {
            'results': CertificateSerializer(certs, many=True).data}
        return Response(serialized_certs)
