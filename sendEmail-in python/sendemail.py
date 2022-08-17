# first of all go to your google account in manage account section

# go to security and turn on option "less secure app access"

import smtplib
import ssl
from email.message import EmailMessage

subject = " email from python "
body ="this is a test email from python"
sender_email = "hello@gmail.com"
receiver_email = "yousifm836@gmail.com"
password = input("enter a password : ")

message = EmailMessage()
message['From'] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
   server.login(sender_email, password)
   server.sendmail(sender_email, receiver_email, message.as_string())
