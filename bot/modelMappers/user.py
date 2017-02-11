import logging

from sqlalchemy import and_

from bot.database import Database
from bot.modelMappers import *
from bot.models.user import User


class UserMapper(object):

    # Create
    def create_user(self, fb_id, first_name=EMPTY_STRING, last_name=EMPTY_STRING):
        try:
            if is_user_args_valid(fb_id, first_name, last_name):
                u = User(fb_id, first_name, last_name)
                Database.add_to_db(u)

        except ValueError as err:
            logging.error(err)
            logging.error(err.args)
            raise ValueError(UNABLE_TO_CREATE.format("User"), fb_id)
        else:
            return u

    # Read
    def get_user_by_fb_id(self, fb_id):
        try:
            if is_fb_id_valid(fb_id):
                u = User.query.filter(User.fb_id == fb_id).first()

        except ValueError as err:
            logging.error(err)
            logging.error(err.args)
            raise err
        if u:
            return u
        else:
            raise ValueError(NOT_FOUND.format("User"), fb_id)

    def get_user_by_name(self, first_name, last_name=EMPTY_STRING):
        try:
            if is_name_valid(first_name):
                if last_name != EMPTY_STRING:
                    u = User.query.filter(and_(User.first_name == first_name,
                                               User.last_name == last_name)).first()
                else:
                    u = User.query.filter(
                        User.first_name == first_name).first()

        except ValueError as err:
            logging.error(err)
            logging.error(err.args)
            raise err
        
        if u:
            return u
        else:
            raise ValueError(NOT_FOUND.format("User"), first_name, last_name)

           

    def get_all_users(self):
        u = User.query.all()
        return u

    # Update
    def set_first_name(self, fb_id, first_name):
        try:
            if is_name_valid(first_name):
                u = self.get_user_by_fb_id(fb_id)
        except ValueError as err:
            logging.error(err)
            logging.error(err.args)
            raise err

        u.set_first_name(first_name)
        Database.commit_db()
        return u

            
    def set_last_name(self, fb_id, last_name):
        try:
            if is_name_valid(last_name):
                u = self.get_user_by_fb_id(fb_id)
        except ValueError as err:
            logging.error(err)
            logging.error(err.args)
            raise err
        
        u.set_last_name(last_name)
        Database.commit_db()
        return u
