from django.contrib.auth.hashers import make_password

from app.models.customer import *
from app.models.certificate import *

from rest_framework import serializers


class CustomerSerializer(serializers.Serializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(max_length=CUSTOMER_NAME_MAX_LENGTH,
                                 style={'base_template': 'textarea.html'})
    email = serializers.CharField(max_length=CUSTOMER_EMAIL_MAX_LENGTH,
                                  style={'base_template': 'textarea.html'})
    password = serializers.CharField(max_length=CUSTOMER_PASSWORD_MAX_LENGTH,
                                     write_only=True)

    def create(self, validated_data):
        """
        Create a return a new Customer, given the validated data.
        :param validated_data: For Customers, we support 'name', 'email', and
          'password'.  'password' MUST be appropriately hashed before calling
          this method.
        :return: the new Customer
        """
        return Customer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Customer, given the validated data
        :param instance:
        :param validated_data: For Customers, we support updating 'name',
          'email', and 'password'.
        :return: the updated Customer
        """
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance


class CertificateSerializer(serializers.Serializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    active = serializers.BooleanField()
    cert_body = serializers.CharField(
        max_length=CERTIFICATE_CERT_BODY_MAX_LENGTH, read_only=True)

    def create(self, validated_data):
        """
        Create and return a new Certificate, given the validated data.
        :param validated_data: For Certificates, we support 'active' and
          'cert_body'.
        :return: the new Certificate
        """
        return Certificate.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Certificate, given the validated data.

        :param instance:
        :param validated_data: For Certificates, we only support 'active'.
        :return: the updated Certificate
        """
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
