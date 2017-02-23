import logging


from flask import render_template, request
from bot import app
from bot.logic.event import EventLogic


logic = EventLogic()


@app.route('/events', methods=['GET'])
def event_index():
    events = logic.get_all_events()
    return render_template('event/index.html', events=events, logic=logic)


@app.route('/event/activate/<event_id>', methods=['GET'])
def activate_event(event_id):
    logic.activate_event(event_id)
    events = logic.get_all_events()
    return render_template('event/index.html', events=events)


@app.route('/event/deactivate/<event_id>', methods=['GET'])
def deactivate_event(event_id):
    logic.deactivate_event(event_id)
    events = logic.get_all_events()
    return render_template('event/index.html', events=events)
