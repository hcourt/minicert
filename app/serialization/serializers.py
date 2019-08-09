from rest_framework import serializers

from app.models.certificate import *


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
    # TODO: serialize private_key

    class Meta:
        model = Certificate
        fields = '__all__'


class CertificateUpdateSerializer(serializers.ModelSerializer):
    """
    A CertificateUpdateSerializer:
    - Allows writes to 'active' only.
    """

    class Meta:
        model = Certificate
        fields = ('active',)
