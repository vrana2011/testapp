from django.test import TestCase

class TestSanity(TestCase):
    """docstring for TestSanity"""
    def __init__(self):
        super(TestSanity, self).__init__()

    def test_assertion(self):
        assert 1
