from flask_mail import Message
from flask import render_template
# from decouple import config
from . import mail

def mail_message(subject,template,to,**kwargs):
    sender_email = config("MAIL_USERNAME", default="")

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    # mail.send(email)