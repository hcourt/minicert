from rest_framework import serializers

from app.models.customer import Customer


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