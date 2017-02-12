import logging

from bot.database import Database
from bot.modelMappers import *
from bot.modelMappers.user import UserMapper
from bot.models.order import Order


class OrderMapper(object):

    def __init__(self):
        self.userMapper = UserMapper()

    def create_order(self, fb_id):
        try:
            user = self.userMapper.get_user_by_fb_id(fb_id)
        except ValueError as err:
            logging.error(err)
            logging.error(err.args)
            raise ValueError(UNABLE_TO_CREATE.format("Order"), fb_id)
        else:
            order = Order(user)
            order.set_time_auto()
            Database.add_to_db(order)
            return order

    # READ
    def get_order_by_order_id(self, order_id):
        order = Order.query.filter(Order.id == order_id).first()
        if order:
            return order
        else:
            raise ValueError(NOT_FOUND.format("Order"), order_id)

    def get_orders_by_fb_id(self, fb_id):
        try:
            user = self.userMapper.get_user_by_fb_id(fb_id)
        except ValueError as err:
            logging.error(err)
            logging.error(err.args)
            raise err
        
        user_id = user.id
        order = Order.query.filter(Order.user_id == user_id)
        if order.count() > 0:
            return order
        else:
            raise ValueError(NOT_FOUND.format("Orders"), fb_id)

    def get_all_orders(self):
        o = Order.query.all()
        return o

    # UPDATE
    def update_order_status_by_order_id(self, order_id, status):
        try:
            order = self.get_order_by_order_id(order_id)
        except ValueError as err:
            logging.error(err)
            logging.error(err.args)
            raise err

        order.set_status(status)
        order.set_time_auto()
        Database.commit_db()
        return order
