import json
import unittest

import mock

from kalliope.core.NeuronModule import MissingParameterException, InvalidParameterException
from kalliope.neurons.cryptocurrency import Cryptocurrency


class TestCryptocurrency(unittest.TestCase):

    def setUp(self):
        self.currency="BTC"
        self.target="EUR"

    def testMissingParameters(self):
        def run_test(parameters_to_test):
            with self.assertRaises(MissingParameterException):
                Cryptocurrency(**parameters_to_test)

        # empty
        parameters = dict()
        run_test(parameters)

        # Missing currency
        parameters = {
            "currency": self.currency,
        }
        run_test(parameters)

        # Missing target
        parameters = {
            "target": self.target,
        }
        run_test(parameters)
