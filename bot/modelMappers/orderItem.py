from bot import db

import bot.models.orderItem
import bot.modelMappers
import bot.modelMappers.order
import bot.constants.value
import bot.constants.error

import logging

class OrderItemMapper(object):

	def __init__(self):
		self.orderMapper = OrderMapper()
	
	# CREATE
	def create_order_item(self, order_id, description, quantity):
		order = None
		try:
			order = self.orderMapper.get_order_by_order_id(order_id)
		except ValueError as err:
			logging.error(err)
			logging.error(err.args)
		
		quantity_valid = False
		try:
			quantity_valid = is_quantity_valid(quantity)
		except ValueError as err:
			logging.error(err)
			logging.error(err.args)

		if order and quantity_valid:
			orderItem = OrderItem(order, description, quantity)
			db.session.add(orderItem)
			db.session.commit()
			return orderItem

		return None

	# READ
	def get_order_item_by_order_id(self, order_id):
		order_item = OrderItem.query.filter(OrderItem.order_id == order_id)
		return order_item if order_item else raise ValueError(NOT_FOUND.format("Order item"))

	# UPDATE
	def update_order_item_quantity_by_order_id(self, order_id, quantity):
		order_item = None
		try:
			order_item = self.get_order_by_order_id(order_id)
		except ValueError as err:
			logging.error(err)
			logging.error(err.args)
		
		quantity_valid = False
		try:
			quantity_valid = is_quantity_valid(quantity)
		except ValueError as err:
			logging.error(err)
			logging.error(err.args)

		if order_item and quantity_valid:
			order_item.set_quantity(quantity)
			db.session.commit()
			return order_item
		return None
