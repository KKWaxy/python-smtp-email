# Hello Guys !!!

# Welcome back to our python cours.

# Today we are going to see HOW TO SEND EMAL BY USING python smtplib.SMTP and Gmail

# ENJOY !!!!!!!!!!!!!!!!!!!!!!!!

# Let's import our packages
import smtplib, ssl, getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# My local(smptp sender server) SMTP Server
local_server = "smtp.gmail.com"
local_server_port = 587

# Go on your google email sender account and enable "less secure apps"

# My Local gmail user credentials
sender_email = "" 
sender_password = getpass.getpass(prompt="Password ("+sender_email.strip()+"): ")

# My ssl conetxt instead of using ssl files
ssl_context = ssl.create_default_context()
message_body = """\
<!DOCTYPE html>
<body>
Your HTML BOdy
</body>
</html>
"""
#My Email Message
try:
    with open("email.txt","r") as file:
        for emailadress in file.readlines():
            message = MIMEMultipart("alternative")
            message["from"] = sender_email
            message["subject"] = "<Edit this>"
            message_body_html = MIMEText(message_body,'html')
            message.attach(message_body_html)
            server = smtplib.SMTP(local_server,local_server_port)
            server.ehlo()
            server.starttls(context=ssl_context)
            server.ehlo()
            message["to"] = emailadress.strip()
            server.login(sender_email,sender_password)
            server.send_message(message)
            print("Done for {}.".format(emailadress.strip()))
except Exception as e:
    print(e)