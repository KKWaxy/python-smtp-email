# Hello Guys !!!

# Welcome back to our python cours.

# Today we are going to see HOW TO SEND EMAL BY USING python smtplib.SMTP and Gmail

# ENJOY !!!!!!!!!!!!!!!!!!!!!!!!

# Let's import our packages

import smtplib, ssl, getpass
from email.message import EmailMessage

# My local(smptp sender server) SMTP Server
local_server = "smtp.gmail.com"
local_server_port = 587

# Go on your google email sender account and enable "less secure apps"

# My Local gmail user credentials
sender_email = "yasahiroyasuo@gmail.com"
sender_password = getpass.getpass(prompt="Password ("+sender_email.strip()+"): ")

# My ssl conetxt instead of using ssl files
ssl_context = ssl.create_default_context()

#My Email Message

message = EmailMessage()
message["from"] = sender_email
message["to"] = "kkwaxy@gmail.com"
message["subject"] = "Trying Pyhton SMTP package"
message.set_content("Let try it now !!!")

try:
    server = smtplib.SMTP(local_server,local_server_port)
    server.ehlo()
    server.starttls(context=ssl_context)
    server.ehlo()
    server.login(sender_email,sender_password)
    server.send_message(message)
    print("Done !")
except Exception as e:
    print(e)