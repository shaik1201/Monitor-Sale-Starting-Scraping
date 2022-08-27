# Importing libraries
import smtplib
import time
import hashlib
from urllib.request import urlopen, Request
import os

EMAIL_ADD = os.environ.get('EMAIL_ADD')
EMAIL_PASS = os.environ.get('EMAIL_PASS')

# setting the URL you want to monitor
url = Request('https://mhaifafc.com/page?pageID=6250', headers={'User-Agent': 'Mozilla/5.0'})

# to perform a GET request and load the
# content of the website and store it in a var
response = urlopen(url).read()

# to create the initial hash
currentHash = hashlib.sha224(response).hexdigest()
print("running")
time.sleep(10)

while True:
    try:
        response = urlopen(url).read()

        currentHash = hashlib.sha224(response).hexdigest()

        time.sleep(30)

        response = urlopen(url).read()

        newHash = hashlib.sha224(response).hexdigest()

        if newHash == currentHash:
            continue

        else:
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login(EMAIL_ADD, EMAIL_PASS)
                subject = 'check if tickets sale has started.'
                body = 'go to https://mhaifafc.com/page?pageID=6250 and buy tickets.'
                msg = f'subject: {subject} \n\n {body}'
                smtp.sendmail(EMAIL_ADD, EMAIL_ADD, msg)
                break
    except Exception as e:
        print("error")