# -*- coding: utf-8 -*-
from flask.ext.wtf import Form, TextField, TextAreaField, Required, Length

class PubkeyForm(Form):
    title = TextField(u'名称', validators = [Required(), Length(min=1)])
    key = TextAreaField(u'公钥', validators = [Required(), Length(min=1)])

