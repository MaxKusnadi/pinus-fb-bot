from bot import db

import bot.models.order
import bot.modelMappers
import bot.modelMappers.user
import bot.constants.value
import bot.constants.error

import logging

class OrderMapper(object):
	def __init__(self):
		self.userMapper = UserMapper()

	def create_order(self, fb_id):
		order = None
		try:
			user = self.userMapper.get_user_by_fb_id(fb_id)
		except ValueError as err:
			logging.error(err)
			logging.error(err.args)
		else:
			order = Order(user)
			order.set_time_auto()
			db.session.add(order)
			db.session.commit()
		return order

	# READ
	def get_order_by_order_id(self, order_id):
		order = Order.query.filter(Order.id == order_id).first()
		return order if order else raise ValueError(NOT_FOUND.format("Order"), order_id)

	def get_orders_by_fb_id(self, fb_id):
		try:
			user_id = self.userMapper.get_user_id(fb_id)
		except ValueError as err:
			logging.error(err)
			logging.error(err.args)
		order = Order.query.filter(Order.user_id == user_id)
		return order if order else raise ValueError(NOT_FOUND.format("Orders"), fb_id)

	# UPDATE
	def update_order_status_by_order_id(self, order_id, status):
		try:
			order = self.get_order_by_order_id(order_id)
		except ValueError as err:
			logging.error(err)
			logging.error(err.args)
		order.set_status(status)
		order.set_time_auto()
		db.session.commit()
		return order