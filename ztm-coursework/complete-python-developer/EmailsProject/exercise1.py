# Exercise 1: sending an email with python
# -------------------

# import smtplib
#
# from email.message import EmailMessage
#
# email = EmailMessage()
# email["from"] = "Vishnu Vardhan"
# email["to"] = "EXAMPLE@gmail.com"
# email["subject"] = "Hello from my python script"
# email.set_content("I am very glad that this works.")
#
# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("EXAMPLE@gmail.com","ACTUAL APP PASSWORD HERE")
#     smtp.send_message(email)
#     print("Email Sent!!")

# Exercise 2: Sending Customised email
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Vishnu Vardhan"
email["to"] = "EXAMPLE@gmail.com"
email["subject"] = "Hello from my python script"
email.set_content(html.substitute({'name':"KSP Garu"}),"html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("EXAMPLE@MAIL.COM","PUT ACTUAL LOGIN PASSWORD HERE")
    smtp.send_message(email)
    print("Email Sent!!")