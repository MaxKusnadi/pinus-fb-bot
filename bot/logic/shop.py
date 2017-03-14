import logging
import json

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

    def generate_payload_start_order(self, recipient_id):
        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "text": "Which flower do you want?",
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "Packet A",
                        "payload": "Packet A"
                    },
                    {
                        "content_type": "text",
                        "title": "Packet B",
                        "payload": "Packet B"
                    },
                    {
                        "content_type": "text",
                        "title": "Packet C",
                        "payload": "Packet C"
                    },
                    {
                        "content_type": "text",
                        "title": "Packet D",
                        "payload": "Packet D"
                    }
                ]
            }
        })
        return data

    def process_quick_reply(self, sender_id, payload):
        if payload in ["Packet A", "Packet B", "Packet C", "Packet D"]:
            logging.info("processing quantity for {recipient}".format(
                recipient=sender_id))
            data = self._process_quantity(sender_id, payload)
        elif payload == "No":
            logging.info("Canceling order for {}".format(sender_id))
            data = self._process_text(
                sender_id, "You can always order flower again by typing 'shop'! ")
        elif self._check_confirmation(payload):
            logging.info("Storing order for {}".format(sender_id))
            self._store_order(sender_id, payload)
            data = self._process_text(
                sender_id, "Your order has been confirmed. Thanks for ordering! :)")
        elif self._check_quantity(payload):
            logging.info("Confirming order for {recipient}".format(
                recipient=sender_id))
            data = self._confirm_order(sender_id, payload)
        else:
            data = self._process_text(
                sender_id, "Sorry an error occured! It should'nt be happening. Please try again or order here bit.ly/PINUSFlowers")
        return data

    def _store_order(self, sender_id, payload):
        payload = eval(payload)
        order = self.order.create_order(
            sender_id, payload['description'], payload['quantity'])

    def _check_confirmation(self, payload):
        return "confirmed" in payload

    def _check_quantity(self, payload):
        lst = ["1", "2", "3", "4", "5"]
        result = False
        for num in lst:
            if num in payload:
                result = True
        return result

    def _process_text(self, sender_id, message_text):
        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "text": message_text
            }
        })
        return data

    def _process_quantity(self, sender_id, payload):
        data = json.dumps({
            "recipient": {
                "id": sender_id
            },
            "message": {
                "text": "How many {} do you want?".format(payload),
                "quick_replies":[
                    {
                        "content_type":"text",
                        "title":"1",
                        "payload": str({
                            "description": payload,
                            "quantity": 1
                            })
                    },
                    {
                        "content_type":"text",
                        "title":"2",
                        "payload": str({
                            "description": payload,
                            "quantity": 2
                            })
                    },
                    {
                        "content_type":"text",
                        "title":"3",
                        "payload": str({
                            "description": payload,
                            "quantity": 3
                            })
                    },
                    {
                        "content_type":"text",
                        "title":"4",
                        "payload": str({
                            "description": payload,
                            "quantity": 4
                            })
                    },
                    {
                        "content_type":"text",
                        "title":"5",
                        "payload": str({
                            "description": payload,
                            "quantity": 5
                            })
                    }
                ]
            }
        })
        return data

    def _confirm_order(self, sender_id, payload):
        payload = eval(payload)
        payload["confirmed"] = True
        data = json.dumps({
            "recipient": {
                "id": sender_id
            },
            "message": {
                "text": "Confirm order?",
                "quick_replies": [
                    {
                        "content_type": "text",
                        "title": "Yes",
                        "payload": str(payload),
                        "image_url": "https://cdn.pixabay.com/photo/2013/06/23/19/47/rose-140853_960_720.jpg"
                    },
                    {
                        "content_type": "text",
                        "title": "No",
                        "payload": "No",
                        "image_url": "https://cdn.pixabay.com/photo/2013/05/26/12/14/rose-113735_960_720.jpg"
                    }
                ]
            }
        })
        return data
