from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Email, URL


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class CourseForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    image_link = StringField('Image Link', validators=[DataRequired(), URL(require_tld=True)])
    certification_link = StringField('Certification Link', validators=[DataRequired(), URL(require_tld=True)])
    conclusion_date = DateField('Conclusion Date', validators=[DataRequired()] ,format='%d/%m/%Y')
    description = StringField('Description', widget=TextArea(), validators=[DataRequired()])
    submit = SubmitField('Submit')


class UpdateUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    image_link = StringField('Image Link', validators=[DataRequired(), URL(require_tld=True)])
    description = StringField('Description', widget=TextArea(), validators=[DataRequired()])
    submit = SubmitField('Update Data')
