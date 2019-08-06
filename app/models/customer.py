from django.db import models

CUSTOMER_NAME_MAX_LENGTH = 128
CUSTOMER_EMAIL_MAX_LENGTH = 254
CUSTOMER_PASSWORD_MAX_LENGTH = 256


# A Customer:
# - Has a name
# - Has an email address
# - Has a password
# - May have zero to many Certificates
class Customer(models.Model):
    name = models.CharField(max_length=CUSTOMER_NAME_MAX_LENGTH)
    email = models.CharField(max_length=CUSTOMER_EMAIL_MAX_LENGTH)
    password = models.BinaryField(max_length=CUSTOMER_PASSWORD_MAX_LENGTH)

    def __str__(self):
        return "{} ({})".format(self.name, self.email)
