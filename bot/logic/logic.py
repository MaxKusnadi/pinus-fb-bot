import logging

from bot.logic.event import EventLogic
from bot.logic.facebook import FacebookLogic
from bot.logic.shop import ShopLogic


class Logic(object):

    def __init__(self):
        self.event = EventLogic()
        self.facebook = FacebookLogic()
        self.shop = ShopLogic()

    def parse_messaging_event(self, messaging_event):
        sender_id = messaging_event["sender"]["id"]
        recipient_id = messaging_event["recipient"]["id"]
        user = self.facebook.get_user_data(sender_id)
        logging.info("Parsing message from {} {}".format(
            user['first_name'], user['last_name']))
        if messaging_event.get("message"):  # someone sent us a message
            self._parse_message(user, messaging_event)

        if messaging_event.get("delivery"):  # delivery confirmation
            pass

        if messaging_event.get("optin"):  # optin confirmation
            pass

        # user clicked/tapped "postback" button in earlier message
        if messaging_event.get("postback"):
            pass

    def _parse_message(self, user, messaging_event):
        try:
            message_text = messaging_event["message"]["text"]
        except KeyError:
            self.facebook.send_message_text(
                user['fb_id'], "Thanks for the likes, {name}!".format(name=user['first_name']))
        else:
            if message_text.lower() == "event" or message_text.lower() == "events":
                self._process_event(user)
            elif message_text.lower() == "shop":
                self._process_order(user)

    def _send_event(self, fb_id):
        events = self.event.get_all_active_events()
        count = 1
        for event in events:
            title = "{}. {} \n\n".format(str(count), event.title)
            description = "Desc: {}\n\n".format(
                event.description) if event.description else ""
            link = "Link: {}".format(event.link) if event.link else ""

            message = "".join([title, description, link])
            count += 1
            self.facebook.send_message_text(fb_id, message)
        self.facebook.send_message_text(fb_id, "Thank you! :)")

    def _process_event(self, user):
        self.facebook.send_message_bubble(user['fb_id'])
        self._send_event(user['fb_id'])

    def _process_order(self, user):
        user = self.shop.store_user(user)

    # def parse_message(self, user, messaging_event):
    #     if "quick_reply" in messaging_event["message"].keys():
    #         self.process_quick_reply(user.fb_id, messaging_event[
    #                                  "message"]["quick_reply"]["payload"])
    #     else:
    #         try:
    #             message_text = messaging_event["message"][
    #                 "text"]  # the message's text
    #         except KeyError:
    #             self.send_message_text(
    #                 user.fb_id, "Thanks for the likes, {name}!".format(name=user.first_name))
    #         else:
    #             if message_text.lower() == "order":
    #                 self.start_order(user.fb_id)
    #             else:
    #                 self.send_message_text(
    # user.fb_id, "Hi, {name}! You can order flower by typing
    # 'order'!".format(name=user.first_name))

    # def process_quick_reply(self, sender_id, payload):
    #     if payload == "Packet A" or payload == "Packet B":
    #         self.process_quantity(sender_id, payload)
    #     elif payload in ["1", "2", "3"]:
    #         self.confirm_order(sender_id, payload)
    #     elif payload == "No":
    #         self.send_message_text(
    #             sender_id, "You can always order flower again by typing 'order'! ")
    #     else:
    #         self.store_order(sender_id, payload)

    # def store_order(self, sender_id, payload):
    #     payload = eval(payload)
    #     order = self.order.create_order(sender_id)
    #     order = self.order.update_order_status_by_order_id(
    #         order.id, "CONFIRMED")
    #     orderItem = None
    #     user = self.user.get_user_by_fb_id(sender_id)
    #     self.send_message_text(
    # sender_id, "Thanks for ordering {}! Your order has been confirmed!
    # : )".format(user.first_name))

    # def confirm_order(self, sender_id, payload):
    #     logging.info("starting order for {recipient}".format(
    #         recipient=sender_id))

    #     data = json.dumps({
    #         "recipient": {
    #             "id": sender_id
    #         },
    #         "message": {
    #             "text": "Confirm order?",
    #             "quick_replies": [
    #                 {
    #                     "content_type": "text",
    #                     "title": "Yes",
    #                     "payload": payload,
    #                     "image_url": "https://cdn.pixabay.com/photo/2013/06/23/19/47/rose-140853_960_720.jpg"
    #                 },
    #                 {
    #                     "content_type": "text",
    #                     "title": "No",
    #                     "payload": "No",
    #                     "image_url": "https://cdn.pixabay.com/photo/2013/05/26/12/14/rose-113735_960_720.jpg"
    #                 }
    #             ]
    #         }
    #     })
    #     r = requests.post(self.LINK, params=self.PARAMS,
    #                       headers=self.HEADERS, data=data)
    #     if r.status_code != 200:
    #         logging.info(r.status_code)
    #         logging.info(r.text)

    # def process_quantity(self, sender_id, payload):
    #     logging.info("processing quantity for {recipient}".format(
    #         recipient=sender_id))

    #     data = json.dumps({
    #         "recipient": {
    #             "id": sender_id
    #         },
    #         "message": {
    #             "text": "How many {} do you want?".format(payload),
    #             "quick_replies": [
    #                 {
    #                     "content_type": "text",
    #                     "title": "1",
    #                     "payload": str({
    #                         "description": payload,
    #                         "quantity": 1
    #                     })
    #                 },
    #                 {
    #                     "content_type": "text",
    #                     "title": "2",
    #                     "payload": str({
    #                         "description": payload,
    #                         "quantity": 2
    #                     })
    #                 },
    #                 {
    #                     "content_type": "text",
    #                     "title": "3",
    #                     "payload": str({
    #                         "description": payload,
    #                         "quantity": 3
    #                     })
    #                 },
    #             ]
    #         }
    #     })
    #     r = requests.post(self.LINK, params=self.PARAMS,
    #                       headers=self.HEADERS, data=data)
    #     if r.status_code != 200:
    #         logging.info(r.status_code)
    #         logging.info(r.text)

    # def start_order(self, recipient_id):
    #     logging.info("starting order for {recipient}".format(
    #         recipient=recipient_id))

    #     data = json.dumps({
    #         "recipient": {
    #             "id": recipient_id
    #         },
    #         "message": {
    #             "text": "Which flower do you want?",
    #             "quick_replies": [
    #                 {
    #                     "content_type": "text",
    #                     "title": "Packet A",
    #                     "payload": "Packet A",
    #                     "image_url": "https://cdn.pixabay.com/photo/2013/06/23/19/47/rose-140853_960_720.jpg"
    #                 },
    #                 {
    #                     "content_type": "text",
    #                     "title": "Packet B",
    #                     "payload": "Packet B",
    #                     "image_url": "https://cdn.pixabay.com/photo/2013/05/26/12/14/rose-113735_960_720.jpg"
    #                 }
    #             ]
    #         }
    #     })
    #     r = requests.post(self.LINK, params=self.PARAMS,
    #                       headers=self.HEADERS, data=data)
    #     if r.status_code != 200:
    #         logging.info(r.status_code)
    #         logging.info(r.text)
