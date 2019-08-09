from django.utils.encoding import smart_text, smart_bytes
from rest_framework import serializers

from app.models.certificate import Certificate, \
    CERTIFICATE_PRIVATE_KEY_MAX_LENGTH


class PrivateKeyField(serializers.CharField):
    def to_representation(self, value):
        """
        Convert the internal binary representation to the passed string.

        :param value: internal value
        :return: external representation
        """
        return smart_text(value)

    def to_internal_value(self, data):
        """
        Convert the passed string to the internal binary representation.

        :param data: object with request data
        :return: internal value
        """
        private_key = str(data.get('private_key'))
        return smart_bytes(private_key)


class CertificateSerializer(serializers.ModelSerializer):
    """
    A CertificateSerializer:
    - Allows reads to all fields.
    - Allows writes to all fields.
    """
    private_key = PrivateKeyField(max_length=CERTIFICATE_PRIVATE_KEY_MAX_LENGTH)

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
