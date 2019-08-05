from django.db import models


# A Customer:
# - Has a name
# - Has an email address
# - Has a password
# - May have zero to many Certificates
class Customer(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=254)
    password = models.BinaryField(max_length=256)


# A Certificate:
# - Belongs to one and only one Customer
# - Can be either active or inactive
# - Has a private key
# - Has a certificate body
class Certificate(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    active = models.BooleanField
    private_key = models.BinaryField(max_length=2048)
    cert_body = models.CharField(max_length=2048)
