import logging

from bot.modelMappers.user import UserMapper
from bot.modelMappers.order import OrderMapper


class ShopLogic(object):

    def __init__(self):
        self.user = UserMapper()
        self.order = OrderMapper()

    def store_user(self, user):
        try:
            u = self.user.get_user_by_fb_id(user['fb_id'])
        except ValueError as err:
            logging.error(err)
            try:
                u = self.user.create_user(
                    user['fb_id'], user['first_name'], user['last_name'])
            except Exception as err:
                logging.error(err)
                u = None
        return u

    def get_all_users(self):
        users = self.user.get_all_users()
        return users

    def get_all_orders(self):
        orders = self.order.get_all_orders()
        return orders
