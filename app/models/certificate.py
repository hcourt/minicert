from django.db import models

from app.models.customer import Customer

CERTIFICATE_PRIVATE_KEY_MAX_LENGTH = 2048
CERTIFICATE_CERT_BODY_MAX_LENGTH = 2048


class Certificate(models.Model):
    """
    A Certificate:
    - Belongs to one and only one Customer
    - Can be either active or inactive
    - Has a private key
    - Has a certificate body

    We also assume:
    - A certificate's private key is 2048 bytes.
    - A certificate's cert body is 2048 bytes.
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    private_key = models.BinaryField(
        max_length=CERTIFICATE_PRIVATE_KEY_MAX_LENGTH)
    cert_body = models.CharField(max_length=CERTIFICATE_CERT_BODY_MAX_LENGTH)

    def __str__(self):
        return "certificate for {} (active={})".format(self.customer.name,
                                                       self.active)
