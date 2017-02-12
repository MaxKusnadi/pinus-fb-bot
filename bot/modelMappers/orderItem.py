from bot.database import Database
from bot.models.order import Order
from bot.models.orderItem import OrderItem
from bot.modelMappers import *
from bot.modelMappers.order import OrderMapper


import logging


class OrderItemMapper(object):

    def __init__(self):
        self.orderMapper = OrderMapper()

    # CREATE
    def create_order_item(self, order_id, description, quantity):
        try:
            order = self.orderMapper.get_order_by_order_id(order_id)
        except ValueError as err:
            logging.error(err)
            logging.error(err.args)
            raise err

        try:
            quantity_valid = is_quantity_valid(int(quantity))
        except ValueError as err:
            logging.error(err)
            logging.error(err.args)
            raise err

        orderItem = OrderItem(order, description, quantity)
        Database.add_to_db(orderItem)
        return orderItem

    # READ
    def get_order_items_by_order_id(self, order_id):
        order_items = OrderItem.query.filter(OrderItem.order_id == order_id)
        if order_items.count() > 0:
            return order_items
        else:
            raise ValueError(NOT_FOUND.format("Order item"))

    def get_order_item_by_id(self, order_item_id):
        order_item = OrderItem.query.filter(
            OrderItem.id == order_item_id).first()
        if order_item:
            return order_item
        else:
            raise ValueError(NOT_FOUND.format("Order item"))

    def get_all_order_items(self):
        order_items = OrderItem.query.all()
        return order_items

    # UPDATE
    def update_order_item_quantity_by_order_item_id(self, order_item_id, quantity):
        try:
            order_item = self.get_order_item_by_id(order_item_id)
        except ValueError as err:
            logging.error(err)
            logging.error(err.args)
            raise err

        try:
            quantity_valid = is_quantity_valid(quantity)
        except ValueError as err:
            logging.error(err)
            logging.error(err.args)
            raise err

        order_item.set_quantity(quantity)
        Database.commit_db()
        return order_item
