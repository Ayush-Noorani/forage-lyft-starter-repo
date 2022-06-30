import unittest

from tyres.carrigan import carrigan
from tyres.octoprime import octoprime


class TestCarrigan(unittest.TestCase):
    def test_needs_service_true(self):
        wear = []
        wear.append(0.1)
        wear.append(0.8)
        tyre = carrigan(wear)
        self.assertTrue(tyre.needs_service())

    def test_needs_service_false(self):
        wear = []
        wear.append(0.1)
        wear.append(0.1)
        tyre = carrigan(wear)
        self.assertFalse(tyre.needs_service())


class TestOctoprime(unittest.TestCase):
    def test_needs_service_true(self):
        wear = []
        wear.append(1)
        wear.append(2)
        tyre = octoprime(wear)
        self.assertTrue(tyre.needs_service())

    def test_needs_service_false(self):
        wear = []
        wear.append(1)
        wear.append(0.1)
        tyre = octoprime(wear)
        self.assertFalse(tyre.needs_service())