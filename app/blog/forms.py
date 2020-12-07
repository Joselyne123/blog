from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,ValidationError
from wtforms.validators import Required

class PostForm(FlaskForm):
    title = StringField('Title',validators=[Required()])
    body = TextAreaField('Text',validators=[Required()])
    submit = SubmitField("Submit")


class CommentForm(FlaskForm):
    body = TextAreaField('Text',validators=[Required()])
    submit = SubmitField("Submit")
