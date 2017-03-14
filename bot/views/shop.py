import logging


from flask import render_template
from bot import app
from bot.logic.shop import ShopLogic


logic = ShopLogic()


@app.route('/database', methods=['GET'])
def database():
    users = logic.get_all_users()
    orders = logic.get_all_orders()
    return render_template('shop/index.html', users=users,
                           orders=orders)
