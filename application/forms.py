from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):
    """ Contact form """

    name = StringField("Name", validators=[DataRequired(), Length(min=3, message=('This name is too short!'))], render_kw={"placeholder": "Name"})
    email = StringField("Email", validators=[Email(message=("This is not a valid email!")), DataRequired()], render_kw={"placeholder": "Email"})
    body = TextAreaField("Message", validators=[Length(min=10, message=('This message is too short!')), DataRequired()], render_kw={"rows": 7})
    # recaptcha = RecaptchaField()
    submit = SubmitField("Submit")


class PostForm(FlaskForm):
    """ Form for adding new article """

    title = StringField("Title", validators=[DataRequired()])
    body = TextAreaField("Body", validators=[DataRequired()], render_kw={"rows":20})
    tags = StringField("Tags")
    submit = SubmitField("Submit")
