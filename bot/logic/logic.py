import logging

from bot.logic.event import EventLogic
from bot.logic.facebook import FacebookLogic
from bot.logic.shop import ShopLogic
from bot.logic.songRequest import SongRequestLogic


class Logic(object):

    def __init__(self):
        self.event = EventLogic()
        self.facebook = FacebookLogic()
        self.shop = ShopLogic()
        self.song = SongRequestLogic()

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
        if "quick_reply" in messaging_event["message"].keys():
            self._process_quick_reply(user['fb_id'], messaging_event[
                "message"]["quick_reply"]["payload"])
        else:
            try:
                message_text = messaging_event["message"]["text"]
            except KeyError:
                self.facebook.send_message_text(
                    user['fb_id'], "Thanks for the likes, {name}!".format(name=user['first_name']))
            else:
                if message_text.lower() == "event" or message_text.lower() == "events":
                    self._process_event(user)
                elif message_text.lower() == "shop flower":
                    self._process_order(user)
                elif "//" in message_text.lower():
                    self._process_songs(user, message_text)

    def _process_songs(self, user, message):
        self.facebook.send_message_bubble(user['fb_id'])
        is_song_okay = self.song.process_message(message)
        if is_song_okay:
            self.facebook.send_message_text(
                user['fb_id'], "Thank you! Your request has been recorded")
        else:
            self.facebook.send_message_text(
                user['fb_id'], "Sorry, there is an error processing your request. Did you forget to put the song title or the message? Did you follow this format '<song title> // <message>' ?")

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
        user_stored = self.shop.store_user(user)
        self._start_order(user['fb_id'])

    def _start_order(self, fb_id):
        logging.info("Start ordering for {}".format(fb_id))
        self.facebook.send_message_text(fb_id, "Thank you for ordering! :)")
        self.facebook.send_message_text(fb_id, "Please choose 1:")
        self.facebook.send_message_text(
            fb_id, "Type A: Single Red Rose Bouquet + Baby's breath ($3)")
        self.facebook.send_message_picture(
            fb_id, "https://s-media-cache-ak0.pinimg.com/736x/9a/8d/96/9a8d9695005265b026e6ca8b6e3c4ba5.jpg")
        self.facebook.send_message_text(
            fb_id, "Type B: Three Red Roses Bouquet + Baby's breath ($10)")
        self.facebook.send_message_picture(
            fb_id, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTyj7oCC5WKhhqfdVkYQp1ireIrQmNA5ji5eeWTb4FcLfoYsaG4")
        self.facebook.send_message_text(
            fb_id, "Type C: Single Red Gerbera Bouquet + Baby's breath ($2)")
        self.facebook.send_message_picture(
            fb_id, "https://s-media-cache-ak0.pinimg.com/originals/33/73/37/337337e83ec1b10a67405f2d419229c8.jpg")
        self.facebook.send_message_text(
            fb_id, "Type D: Single Yellow Gerbera Bouquet + Baby's breath ($2)")
        self.facebook.send_message_picture(
            fb_id, "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSIk6ypFYws--Y3V_9X0snuYEQdwWBLAaDaO21-aAnz63MN0vQkVQ")
        payload = self.shop.generate_payload_start_order(fb_id)
        self.facebook.send_reply(payload)

    def _process_quick_reply(self, sender_id, payload):
        data = self.shop.process_quick_reply(sender_id, payload)
        self.facebook.send_reply(data)
