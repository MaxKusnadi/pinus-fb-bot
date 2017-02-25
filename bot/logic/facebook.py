import logging
import json
import os
import requests

from bot.modelMappers.event import EventMapper


class FacebookLogic(object):

    def __init__(self):
        self.map = EventMapper()
        self.PARAMS = {
            "access_token": os.environ["PAGE_ACCESS_TOKEN"]
        }
        self.HEADERS = {
            "Content-Type": "application/json"
        }
        self.LINK = "https://graph.facebook.com/v2.6/me/messages"

    def parse_messaging_event(self, messaging_event):
        sender_id = messaging_event["sender"]["id"]
        recipient_id = messaging_event["recipient"]["id"]
        self.send_message_bubble(sender_id)
        user = self.get_user_data(sender_id)
        if messaging_event.get("message"):  # someone sent us a message
            self.parse_message(user, messaging_event)

        if messaging_event.get("delivery"):  # delivery confirmation
            pass

        if messaging_event.get("optin"):  # optin confirmation
            pass

        # user clicked/tapped "postback" button in earlier message
        if messaging_event.get("postback"):
            pass

    def send_message_bubble(self, recipient_id):
        logging.info("sending message bubble to {recipient}".format(
            recipient=recipient_id))

        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "sender_action": "typing_on"
        })
        r = requests.post(self.LINK, params=self.PARAMS,
                          headers=self.HEADERS, data=data)
        if r.status_code != 200:
            logging.info(r.status_code)
            logging.info(r.text)

    def parse_message(self, user, messaging_event):
        try:
            message_text = messaging_event["message"]["text"]
        except KeyError:
            self.send_message_text(
                user['fb_id'], "Thanks for the likes, {name}!".format(name=user['name']))
        else:
            if message_text.lower() == "event" or message_text.lower() == "events":
                self.send_event(user['fb_id'])

    def get_user_data(self, fb_id):
        logging.info("getting info of {recipient}".format(recipient=fb_id))
        link = "https://graph.facebook.com/v2.6/" + \
            fb_id + "?fields=first_name,last_name"
        r = requests.get(link, params=self.PARAMS, headers=self.HEADERS)
        if r.status_code != 200:
            logging.info(r.status_code)
            logging.info(r.text)
        result = r.json()
        response = dict()
        response['fb_id'] = fb_id
        response['name'] = result['first_name']
        return response

    def send_message_text(self, recipient_id, message_text):
        logging.info("sending message to {recipient}: {text}".format(
            recipient=recipient_id, text=message_text))

        data = json.dumps({
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "text": message_text
            }
        })
        r = requests.post(self.LINK, params=self.PARAMS,
                          headers=self.HEADERS, data=data)
        if r.status_code != 200:
            logging.info(r.status_code)
            logging.info(r.text)

    def send_event(self, fb_id):
        events = self.map.get_all_active_events()
        count = 0
        for event in events:
            title = "{}. {} \n".format(str(count), event.title)
            description = "Desc: {}\n".format(
                event.description) if event.description else ""
            link = "Link: {}".format(event.link) if event.link else ""

            message = "".join([title, description, link])
            count += 1
            self.send_message_text(fb_id, message)
