import logging
import json
import os
import requests

from bot.modelMappers.order import OrderMapper
from bot.modelMappers.orderItem import OrderItemMapper
from bot.modelMappers.user import UserMapper

class Logic(object):
    def __init__(self):
        self.user = UserMapper()
        self.order = OrderMapper()
        self.item = OrderItemMapper()
        self.PARAMS = {
            "access_token": os.environ["PAGE_ACCESS_TOKEN"]
        }
        self.HEADERS = {
            "Content-Type": "application/json"
        }
        self.LINK = "https://graph.facebook.com/v2.6/me/messages"

    def get_all_users(self):
        u = self.user.get_all_users()
        return u

    def get_all_orders(self):
        return self.order.get_all_orders()

    def get_all_order_items(self):
        return self.item.get_all_order_items()

    def parse_messaging_event(self, messaging_event):
        sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
        recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
        self.send_message_bubble(sender_id)
        user = self.store_user(sender_id)
        if messaging_event.get("message"):  # someone sent us a message
            self.parse_message(user, messaging_event)

        if messaging_event.get("delivery"):  # delivery confirmation
            pass

        if messaging_event.get("optin"):  # optin confirmation
            pass

        if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
            pass

    def parse_message(self, user, messaging_event):
        if "quick_reply" in messaging_event["message"].keys():
            self.process_quick_reply(sender_id, messaging_event["message"]["quick_reply"]["payload"])
        try:
            message_text = messaging_event["message"]["text"]  # the message's text
        except KeyError:
            self.send_message_text(sender_id, "Thanks for the likes, {name}!".format(name=u.first_name))
        else:
            if message_text.lower() == "order":
                self.start_order(user.fb_id)
            else:
                self.send_message_text(sender_id, "Hi, {name}! You can order flower by typing 'order'! ".format(name=u.first_name))

    def process_quick_reply(self, sender_id, payload):
        pass

    def start_order(self, recipient_id):
        logging.info("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "text": "Which flower do you want?",
                "quick_replies":[
                    {
                        "content_type":"text",
                        "title":"Packet A",
                        "payload":"Packet A",
                        "image_url":"https://cdn.pixabay.com/photo/2013/06/23/19/47/rose-140853_960_720.jpg"
                    },
                    {
                        "content_type":"text",
                        "title":"Packet B",
                        "payload":"Packet B",
                        "image_url":"https://cdn.pixabay.com/photo/2013/05/26/12/14/rose-113735_960_720.jpg"
                    }
                ]
            }
        })
        r = requests.post(self.LINK, params=self.PARAMS, headers=self.HEADERS, data=data)
        if r.status_code != 200:
            logging.info(r.status_code)
            logging.info(r.text)


    def send_message_text(self, recipient_id, message_text):
        logging.info("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "text": message_text
            }
        })
        r = requests.post(self.LINK, params=self.PARAMS, headers=self.HEADERS, data=data)
        if r.status_code != 200:
            logging.info(r.status_code)
            logging.info(r.text)

    def send_message_bubble(self, recipient_id):
        logging.info("sending message bubble to {recipient}".format(recipient=recipient_id))

        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "sender_action": "typing_on"
        })
        r = requests.post(self.LINK, params=self.PARAMS, headers=self.HEADERS, data=data)
        if r.status_code != 200:
            logging.info(r.status_code)
            logging.info(r.text)

    def store_user(self, fb_id):
        try:
            u = self.user.get_user_by_fb_id(fb_id)
        except ValueError as err:
            logging.error(err)
            first_name, last_name = self.get_user_data(fb_id)
            u = self.user.create_user(fb_id, first_name, last_name)
        return u

    def get_user_data(self, fb_id):
        logging.info("getting info of {recipient}".format(recipient=fb_id))
        link = "https://graph.facebook.com/v2.6/" + fb_id + "?fields=first_name,last_name"
        r = requests.get(link, params=self.PARAMS, headers=self.HEADERS)
        if r.status_code != 200:
            logging.info(r.status_code)
            logging.info(r.text)
        result = r.json()
        return (result['first_name'], result['last_name'])