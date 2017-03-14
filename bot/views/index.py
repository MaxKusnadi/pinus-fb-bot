from flask import render_template
from bot import app


@app.route('/admin', methods=['GET'])
def index():
    return render_template('index.html')
