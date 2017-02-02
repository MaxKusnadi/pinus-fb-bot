from sqlalchemy import _and

from bot import db

import bot.models.user
import bot.modelMappers
import bot.constants.value
import bot.constants.error

import logging

class UserMapper(object):
	# Create
	def create_user(self, fb_id, first_name=EMPTY_STRING, last_name=EMPTY_STRING):
		u = None
		try:
			if is_user_args_valid(fb_id, first_name, last_name): 
				u = User(fb_id, first_name, last_name)
				db.session.add(u)
				db.session.commit()

		except ValueError as err:
			logging.error(err)
			logging error(err.args)

		except Exception as err:
			logging.error(err)

		return u

	# Read
	def get_user_by_fb_id(self, fb_id):
		u = User.query.filter(User.fb_id == fb_id).first() if is_fb_id_valid(fb_id) else None
		return u if u else raise ValueError(NOT_FOUND.format("User"), fb_id)

	def get_user_by_name(self, first_name, last_name=EMPTY_STRING):
		u = None
		try:
			if is_name_valid(first_name):
				u = User
					.query
					.filter(and_(User.first_name == first_name,
								 User.last_name == last_name)).first() if last_name != EMPTY_STRING else
					User
					.query
					.filter(User.first_name == first_name).first()

		except ValueError as err:
			logging.error(err)

		except Exception as err:
			logging.error(err)

		return u if u else raise ValueError(NOT_FOUND.format("User"), fb_id)

	def get_all_users(self):
		u = User.query.all()
		return u

	def get_user_id(self, fb_id):
		u = self.get_user_by_fb_id(fb_id)
		return u.id if u else raise ValueError(NOT_FOUND.format("User"), fb_id)

	def get_user_first_name(self, fb_id):
		u = self.get_user_by_fb_id(fb_id)
		return u.first_name if u else raise ValueError(NOT_FOUND.format("User"), fb_id)

	def get_user_last_name(self, fb_id):
		u = self.get_user_by_fb_id(fb_id)
		return u.last_name if u else raise ValueError(NOT_FOUND.format("User"), fb_id)

	# Update
	def set_first_name(self, fb_id, first_name):
		u = get_user_by_fb_id(fb_id) if is_name_valid(first_name) else None
		if u:
			u.set_first_name(first_name)
			db.session.commit()
		else:
			raise ValueError(NOT_FOUND.format("User"), fb_id, first_name)
		return u

	def set_last_name(self, fb_id, last_name):
		u = get_user_by_fb_id(fb_id) if is_name_valid(last_name) else None
		if u:
			u.set_last_name(last_name)
			db.session.commit()
		else:
			raise ValueError(NOT_FOUND.format("User"), fb_id, last_name)
		return u

	

