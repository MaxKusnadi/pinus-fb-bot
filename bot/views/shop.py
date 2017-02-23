import logging


from flask import render_template
from bot import app
from bot.logic.logic import Logic


logic = Logic()


@app.route('/database', methods=['GET'])
def database():
    users = logic.get_all_users()
    orders = logic.get_all_orders()
    items = logic.get_all_order_items()
    return render_template('database.html', users=users,
                           orders=orders, items=items)
