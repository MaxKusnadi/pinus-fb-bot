import logging
import json
import os
import requests


class FacebookLogic(object):

    def __init__(self):
        self.PARAMS = {
            "access_token": os.environ["PAGE_ACCESS_TOKEN"]
        }
        self.HEADERS = {
            "Content-Type": "application/json"
        }
        self.LINK = "https://graph.facebook.com/v2.6/me/messages"

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
        response['first_name'] = result['first_name']
        response['last_name'] = result['last_name']
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
