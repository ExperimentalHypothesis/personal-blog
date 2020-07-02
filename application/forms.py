from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, Optional, URL


class MessageForm(FlaskForm):
    """ Form for sending a message to me """

    name = StringField("Name", validators=[DataRequired(), Length(min=3, message=('This name is too short!'))], render_kw={"placeholder": "Name"})
    email = StringField("Email", validators=[Email(message=("This is not a valid email!")), DataRequired()], render_kw={"placeholder": "Email"})
    body = TextAreaField("Message", validators=[Length(min=10, message=('This message is too short!')), DataRequired()], render_kw={"rows": 7})
    # TODO recaptcha = RecaptchaField()
    submit = SubmitField("Submit")


class PostForm(FlaskForm):
    """ Form for adding new article """

    title = StringField("Title", validators=[DataRequired()], render_kw={"placeholder": "Title"})
    body = TextAreaField("Body", validators=[DataRequired()], render_kw={"rows":20})
    tags = StringField("Tags") # TODO implement
    submit = SubmitField("Submit")


class ProjectForm(FlaskForm):
    """ Form for adding new project """

    title = StringField("Title", validators=[DataRequired()], render_kw={"placeholder": "Title"})
    project_url = StringField("Project URL", validators=[Optional(), URL(require_tld=False, message="URL is invalid")], render_kw={"placeholder": "Project URL"})
    github_url = StringField("Github URL", validators=[Optional(), URL(require_tld=False, message="URL is invalid")], render_kw={"placeholder": "Github URL"})
    description = TextAreaField("Description", validators=[DataRequired()], render_kw={"rows":20})
    submit = SubmitField("Submit")


class AdminForm(FlaskForm):
    """ Form for logging as Admin """

    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")