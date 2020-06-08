#challenge8
#https://www.linkedin.com/learning/python-code-challenges/send-an-email?u=2163426

#Send an email

import smtplib
#no need to install, comes built in =-O

SENDER_EMAIL = ""
SENDER_PASSWORD = ""

def sendEmail(receiverAddress, subject, messageBody):
	message_ = "Subject: {}\n\n{}".format(subject, messageBody)
	with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
		server.login(SENDER_EMAIL, SENDER_PASSWORD)
		server.sendmail(SENDER_EMAIL, receiverAddress, message_)

SENDER_EMAIL = input("Enter sender's email address: ")
SENDER_PASSWORD = input("Enter sender's password (This part is not secure!):")
sendEmail("dstrube@gmail.com","Test subject","Test body. This is an email sent from Python.")

#TODO: Verify this on a secure server