from flask_wtf import Form
from wtforms import StringField


class UpdateForm(Form):
    title = StringField('New Title')
    description = StringField('New Description')
