from django.db import models

CUSTOMER_NAME_MAX_LENGTH = 128
CUSTOMER_EMAIL_MAX_LENGTH = 254  # Revised email length determinations
CUSTOMER_PASSWORD_MAX_LENGTH = 128  # Follows Django's standards for passwords


class Customer(models.Model):
    """
    A Customer:
    - Has a name
    - Has an email address
    - Has a password
    - May have zero to many Certificates

    Passwords are stored as a CharField, following Django's auth standards.
    They are expected to be hashed appropriately by a serializer before storing.
    """
    name = models.CharField(max_length=CUSTOMER_NAME_MAX_LENGTH)
    email = models.CharField(max_length=CUSTOMER_EMAIL_MAX_LENGTH)
    password = models.CharField(max_length=CUSTOMER_PASSWORD_MAX_LENGTH)

    def __str__(self):
        return "{} ({})".format(self.name, self.email)
