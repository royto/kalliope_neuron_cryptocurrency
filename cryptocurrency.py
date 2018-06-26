import logging
import requests, json

from kalliope.core.NeuronModule import (NeuronModule,
                                        MissingParameterException,
                                        InvalidParameterException)

logging.basicConfig()
logger = logging.getLogger("kalliope")

class Cryptocurrency(NeuronModule):
    """
    Class used to interact with diagral alarm system
    """
    def __init__(self, **kwargs):

        super(Cryptocurrency, self).__init__(**kwargs)

        # parameters
        self.currency = kwargs.get('currency', None)
        self.target = kwargs.get('target', None)

        logger.debug("CryptoCurrency launch for currency %s", self.currency)

        # check parameters
        if self._is_parameters_ok():
            result = dict( )

            payload = {'fsym': self.currency, 'tsyms': self.target}
            logger.debug(payload)
            response = requests.get('https://min-api.cryptocompare.com/data/price', params=payload)

            content = response.json()
            result[self.currency] = dict()
            result[self.currency][self.target] = content[self.target]

            logger.debug(result)
            self.say(result)


    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron.
        :return: True if parameters are ok, raise an exception otherwise.

        .. raises:: MissingParameterException, InvalidParameterException
        """
        if self.currency is None:
            raise MissingParameterException("CryptoCurrency needs an currency")
        if self.target is None:
            raise MissingParameterException("CryptoCurrency needs a target currency")
        return True

