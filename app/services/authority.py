import asyncio
import logging

import requests
from django.conf import settings
from rest_framework import status


async def update_authority(active=None, pk=None, body=None):
    """
    Asynchronously update a certificate authority on the active or inactive
    status of a certificate.

    :param active: True if the certificate has become active, False if
    the certificate has become inactive.
    :param pk: primary key of the certificate
    :param body: body of the certificate.  Will be sent to the authority.
    :return: after awaiting the post
    """

    async def _post_async(*args, **kwargs):
        return requests.post(*args, **kwargs)

    data = {'certificate': body, 'active': active}
    authority = settings.ACTIVATE_AUTHORITY

    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    task = loop.create_task(_post_async(authority, data))
    response = await task

    if response.status_code == status.HTTP_200_OK:
        logging.info(
            "Notified authority %s that certificate %s is %s",
            authority, pk, "active" if active else "inactive")
    else:
        logging.error(
            "Unable to notify authority %s that certificate %s is %s: "
            "status %s",
            authority, pk, "active" if active else "inactive",
            response.status_code)
    return
