from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models.customer import Customer
from app.serialization.certificate import CertificateSerializer
from app.serialization.customer import CustomerSerializer


class CustomerView(generics.CreateAPIView,
                   generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerCertificatesView(APIView):
    def get(self, request, pk):
        c = get_object_or_404(Customer, pk=pk)
        certs = c.certificate_set.all()
        serialized_certs = {
            'results': CertificateSerializer(certs, many=True).data}
        return Response(serialized_certs)


class CustomerActiveCertificatesView(APIView):
    def get(self, request, pk):
        c = get_object_or_404(Customer, pk=pk)
        certs = c.certificate_set.filter(active=True)
        serialized_certs = {
            'results': CertificateSerializer(certs, many=True).data}
        return Response(serialized_certs)
