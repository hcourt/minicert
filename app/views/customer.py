from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from app.models.customer import Customer
from app.serialization.serializers import CustomerSerializer, \
    CertificateSerializer


class CustomerView(generics.CreateAPIView,
                   generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


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
