from logger_base import logger

class UsernameException(Exception):

    def __init__(self,msj):
        self.message = f'Username Exception: {msj}'
        logger.error(self.message)


class PaymentException(Exception):

    def __init__(self, msj):
        self.message = f'Payment Exception: {msj}'
        logger.error(self.message)


class CreditCardException(Exception):

    def __init__(self, msj):
        self.message = f'Credit Exception: {msj}'
        logger.error(self.message)