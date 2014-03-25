from django.test import TestCase
from core.services import watch_services
from helpers import test_data
from django.test.client import Client
from django.core.urlresolvers import reverse

__author__ = 'tony'

def _reverse(watch_view, **kwargs):
    return reverse('core.views.watch_views.' + watch_view, kwargs=kwargs)


class TestWatchViews(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.user = test_data.createDummyUserRandom(login='johndoe', password='abc123')
        self.client = Client()
        self.client.login(username=self.user.username, password='abc123')

    def test_watch_unwatch_issue(self):
        toggle_watch_url = reverse('core.views.json_views.toggle_watch')
        issue = test_data.create_dummy_issue()
        self.assertTrue(not watch_services.is_watching_issue(self.user, issue.id))

        response = self.client.post(toggle_watch_url, {'entity': 'ISSUE', 'objid': issue.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'WATCHING')
        self.assertTrue(watch_services.is_watching_issue(self.user, issue.id))

        response = self.client.post(toggle_watch_url, {'entity': 'ISSUE', 'objid': issue.id})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'NOT_WATCHING')
        self.assertTrue(not watch_services.is_watching_issue(self.user, issue.id))
