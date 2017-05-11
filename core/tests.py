from django.test import TestCase

class TestSanity(TestCase):
    """docstring for TestSanity"""

    def test_assertion(self):
        assert 1
    def test_assertion_failing(self):
        assert 0
