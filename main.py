"""
Questions:


    1. Complete the `MiniVenmo.create_user()` method to allow our application to create new users.

    2. Complete the `User.pay()` method to allow users to pay each other. Consider the following: if user A is paying user B, user's A balance should be used if there's enough balance to cover the whole payment, if not, user's A credit card should be charged instead.

    3. Venmo has the Feed functionality, that shows the payments that users have been doing in the app. If Bobby paid Carol $5, and then Carol paid Bobby $15, it should look something like this


    Bobby paid Carol $5.00 for Coffee
    Carol paid Bobby $15.00 for Lunch

    Implement the `User.retrieve_activity()` and `MiniVenmo.render_feed()` methods so the MiniVenmo application can render the feed.

    4. Now users should be able to add friends. Implement the `User.add_friend()` method to allow users to add friends.
    5. Now modify the methods involved in rendering the feed to also show when user's added each other as friends.
"""

"""
MiniVenmo! Imagine that your phone and wallet are trying to have a beautiful
baby. In order to make this happen, you must write a social payment app.
Implement a program that will feature users, credit cards, and payment feeds.
"""

import unittest
from exceptions import UsernameException, PaymentException, CreditCardException
from logger_base import logger
from user import User


class MiniVenmo:
    def create_user(self, username, balance, credit_card_number):
        # TODO: add code here
        user = User(username=username)
        user.add_to_balance(balance)
        user.add_credit_card(credit_card_number)
        return user

    def render_feed(self, feed):
        # Bobby paid Carol $5.00 for Coffee
        # Carol paid Bobby $15.00 for Lunch
        # TODO: add code here

        if feed == None:
            logger.error(f'feed is empty')
        for f in feed:
            print(f)

    @classmethod
    def run(cls):
        venmo = cls()

        bobby = venmo.create_user("Bobby", 5.00, "4111111111111111")
        carol = venmo.create_user("Carol", 10.00, "4242424242424242")

        try:
            # should complete using balance
            bobby.pay(carol, 5.00, "Coffee")
            logger.info(f'{bobby.username} paid {carol} $5.00 for "Coffee"')
            # should complete using card
            carol.pay(bobby, 15.00, "Lunch")
            logger.info(f'{carol.username} paid {bobby} $15.00 for "Lunch"')

        except PaymentException as e:
            print(e)

        feed = bobby.retrieve_feed()
        print(f'Feed : {feed}')
        venmo.render_feed(feed)
        #
        bobby.add_friend(carol)
        relations = bobby.retrive_relationship()
        venmo.render_relation(relations)

    def render_relation(self, relations):
        for r in relations:
            print(r)


class TestUser(unittest.TestCase):

    def test_this_works(self):
        with self.assertRaises(UsernameException):
            raise UsernameException('Error User Name Exception')
        with self.assertRaises(PaymentException):
            raise PaymentException('Error Payment Exception')
        with self.assertRaises(CreditCardException):
            raise CreditCardException('Error Credit Card Exception')
        # with self.run(self):


if __name__ == '__main__':
    # unittest.main()
    MiniVenmo.run()
