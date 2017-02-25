from flask_wtf import Form
from wtforms import StringField, TextAreaField


class UpdateForm(Form):
    title = StringField('New Title')
    description = TextAreaField('New Description')
    link = StringField('Form URL or website if any')


class CreateForm(Form):
    title = StringField('Title')
    description = TextAreaField('Description')
    link = StringField('Form URL or website if any')
