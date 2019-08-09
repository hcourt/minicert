from rest_framework import serializers

from app.models.certificate import Certificate


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