from flask_wtf import Form
from wtforms import  StringField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField
from wtforms import validators, ValidationError
from wtforms.validators import InputRequired, Email


class ContactForm(Form):
   name = StringField("Name Of Student",[validators.DataRequired("Please enter your name.")])
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   Address = TextAreaField("Address")
   
   email = StringField("Email",[validators.DataRequired("Please enter your email address."),
      ])
   
   Age = IntegerField("age")
   language = SelectField('Languages', choices = [('cpp', 'C++'), 
      ('py', 'Python')])
   submit = SubmitField("Send")