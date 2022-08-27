import smtplib
import os

EMAIL_ADD = os.environ.get('EMAIL_ADD')
EMAIL_PASS = os.environ.get('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADD, EMAIL_PASS)

    subject = 'dinner this weekend?'
    body = 'dinner 6 pm saturday?'

    msg = f'subject: {subject} \n\n {body}'

    smtp.sendmail(EMAIL_ADD, EMAIL_ADD, msg)