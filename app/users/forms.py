from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,ValidationError
from wtforms.validators import Required


class CommentForm(FlaskForm):
    body = TextAreaField('Text',validators=[Required()])
    submit = SubmitField("Submit")
