import logging


from flask import render_template, request, redirect, url_for, flash
from bot import app
from bot.forms.events import CreateForm, UpdateForm
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
    flash('Event with id: {} is activated'.format(event_id))
    return redirect(url_for('event_index'))


@app.route('/event/deactivate/<event_id>', methods=['GET'])
def deactivate_event(event_id):
    logic.deactivate_event(event_id)
    events = logic.get_all_events()
    flash('Event with id: {} is deactivated'.format(event_id))
    return redirect(url_for('event_index'))


@app.route('/event/update/<event_id>', methods=['GET', 'POST'])
def update_event(event_id):
    form = UpdateForm()
    event = logic.get_event_by_id(event_id)
    if form.validate_on_submit():
        title = form.title.data if form.description.data else None
        description = form.description.data if form.description.data else None
        link = form.link.data if form.link.data else None

        logging.debug('Form content: Title:{}, Description:{}, Link:{}'.format(
            title, description, link))

        if title or description or link:
            e = logic.update_event(event_id, title, description, link)
        else:
            flash("Fields can't be left empty")
            redirect(url_for('update_event'))

        if e:
            flash("Event updated!")
            return redirect(url_for('event_index'))
        else:
            flash("Error occured")
            redirect(url_for('update_event'))

    return render_template('event/update.html', form=form, event=event)


@app.route('/event/create', methods=['GET', 'POST'])
def create_event():
    form = CreateForm()
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data if form.description.data else None
        link = form.link.data if form.link.data else None

        logging.debug('Form content: Title:{}, Description:{}, Link:{}'.format(
            title, description, link))

        e = logic.create_event(title, description, link)
        if e:
            flash("Event created!")
            return redirect(url_for('event_index'))
        else:
            flash("Error occured. Please try again. Did you fill in the title?")
            redirect(url_for('create_event'))

    return render_template('event/create.html', form=form)
