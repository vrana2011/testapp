from django.test import TestCase

from ghost.ext.django.test import GhostTestCase


class SessionSecurityTestCase(GhostTestCase):
    # Enable display (runs headless with False)
    display = True

    # Default port for LiveServerTestCase, from django docs:
    # https://docs.djangoproject.com/en/1.4/topics/testing/#django.test.LiveServerTestCase
    port = 8081

    # Shortcut for open
    def open(self, url):
        self.ghost.open('http://localhost:%s%s' % (self.port, url))

    def test_ghost(self):
        self.open('/admin/')
        self.ghost.wait_for_selector('input[name=username]')
        self.assertTrue(True)


class TestSanity(TestCase):
    """docstring for TestSanity"""

    def test_assertion(self):
        assert 1
