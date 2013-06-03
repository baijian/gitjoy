# -*- coding: utf-8 -*-
from flask.ext.wtf import Form, ValidationError, SubmitField, PasswordField, TextField, TextAreaField, Required, Length

class PubkeyForm(Form):
    title = TextField(u'名称', validators = [Required(), Length(min=1)])
    key = TextAreaField(u'公钥', validators = [Required(), Length(min=1)])


class LoginForm(Form):
    """
    Validate the login form
    """
    email = TextField(u'Email', validators = [Required(), Length(min=1)])
    password = PasswordField(u'Password', validators = [Required(), Length(min=1)])
    submit = SubmitField('Login')

    def validate_email(self, field):
        raise ValidationError("Invalid")


