from django.test import TestCase

from app.serialization.certificate import PrivateKeyField


class PrivateKeyFieldTestCase(TestCase):
    def test(self):
        private_key = "foobar"
        field = PrivateKeyField(max_length=32)
        bytestr = field.to_internal_value(data={'private_key': private_key})
        rep = field.to_representation(bytestr)

        self.assertEqual(private_key, rep)
