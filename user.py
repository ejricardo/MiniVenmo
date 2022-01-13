from exceptions import UsernameException, CreditCardException
import re
from payment import Payment
from logger_base import logger

class User:
    feed = []
    payment=None
    relationship =[]

    def __init__(self, username):
        self.credit_card_number = None
        self.balance = 0.0

        if self._is_valid_username(username):
            self.username = username
        else:
            raise UsernameException('Username not valid.')

    def __str__(self):
        return self.username;

    def retrieve_feed(self):
        # TODO: add code here
        return self.feed

    def add_friend(self, new_friend):
        # TODO: add code here
        self.relationship.append(new_friend)
        logger.info(f'{self.username} added new friend call {new_friend}')
        
    def retrive_relationship(self):
        listRel=[]
        for r in self.relationship:
            listRel.append(f'{self.username} has connection with {r}')
        return listRel

    def add_to_balance(self, amount):
        self.balance += float(amount)

    def add_credit_card(self, credit_card_number):
        if self.credit_card_number is not None:
            raise CreditCardException('Only one credit card per user!')

        if self._is_valid_credit_card(credit_card_number):
            self.credit_card_number = credit_card_number

        else:
            raise CreditCardException('Invalid credit card number.')

    def pay_with_card(self, target, amount, note):
        logger.info(f'-- {self.username} Pay with Card to {target} ${amount} for {note}')
        amount = float(amount)

        if self.username == target.username:
            raise PaymentException('User cannot pay themselves.')

        elif amount <= 0.0:
            raise PaymentException('Amount must be a non-negative number.')

        elif self.credit_card_number is None:
            raise PaymentException('Must have a credit card to make a payment.')

        self._charge_credit_card(self.credit_card_number)
        payment = Payment(amount, self, target, note)
        target.add_to_balance(amount)

        return payment

    def pay_with_balance(self, target, amount, note):
        logger.info(f'-- {self.username} Pay with Balance to {target} ${amount} for {note}')
        # print(self.username + f' paid {target} {amount} {note}')
        payment = Payment(amount, self, target, note)
        return payment
        # pass

    def _is_valid_credit_card(self, credit_card_number):
        return credit_card_number in ["4111111111111111", "4242424242424242"]

    def _is_valid_username(self, username):
        return re.match('^[A-Za-z0-9_\\-]{4,15}$', username)

    def _charge_credit_card(self, credit_card_number):
        # magic method that charges a credit card thru the card processor
        pass

    def retrieve_activity(self):
        self.feed.append(f'{self.payment.actor} paid {self.payment.target} ${self.payment.amount} for {self.payment.note}')


    def pay(self, target, amount, note):
        # TODO: add logic to pay with card or balance
        # if user A is paying user B, user's A balance should be used if there's enough balance to cover the whole payment,
        # if not, user's A credit card should be charged instead

        if self.balance>=amount :
            self.payment=self.pay_with_balance(target,amount,note)
        else:
            self.payment=self.pay_with_card(target,amount,note)
        self.retrieve_activity()
