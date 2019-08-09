import asyncio

from django.test import TestCase

from unittest import mock

from app.services.authority import update_authority


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


def requests_post_mock(response_data=None, response_status=200):
    def f(url, data=None, json=None, **kwargs):
        return MockResponse(response_data, response_status)

    return f


class AuthorityTestCase(TestCase):

    @mock.patch('requests.post', side_effect=requests_post_mock())
    def test_valid(self, mock_post):
        loop = asyncio.new_event_loop()
        result = loop.run_until_complete(
            update_authority(active=True, pk=1, body="this-is-a-cert-body"))
        loop.close()

        self.assertIn(
            mock.call(
                'http://httpbin:80/post',
                data={'certificate': 'this-is-a-cert-body', 'active': True}
            ),
            mock_post.call_args_list
        )

        self.assertEqual(result, True)

    @mock.patch('requests.post',
                side_effect=requests_post_mock(response_status=404))
    def test_invalid(self, mock_post):
        loop = asyncio.new_event_loop()
        result = loop.run_until_complete(
            update_authority(active=True, pk=1, body="this-is-a-cert-body"))
        loop.close()

        self.assertIn(
            mock.call(
                'http://httpbin:80/post',
                data={'certificate': 'this-is-a-cert-body', 'active': True}
            ),
            mock_post.call_args_list
        )

        self.assertEqual(result, False)
