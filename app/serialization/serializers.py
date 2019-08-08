from app.models.certificate import *

from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    """
    A CustomerSerializer:
    - Allows reads to all fields except 'password'.
    - Allows writes to all fields.
    - Orders Customers by 'name'
    """

    class Meta:
        model = Customer
        fields = '__all__'
        ordering = ('name',)
        write_only_fields = ('password',)


class CertificateSerializer(serializers.ModelSerializer):
    """
    A CertificateSerializer:
    - Allows reads to all fields.
    - Allows writes to all fields.
    """

    class Meta:
        model = Certificate
        fields = '__all__'
