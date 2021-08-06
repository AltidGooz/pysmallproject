import smtplib
from email.message import EmailMessage

# Creating a object for EmailMessage
email = EmailMessage()
# Person who is sending
email['from'] = 'xyz name'
# Whom we are sending
email['to'] = 'xyz id'
# Subject of email
email['subject'] = 'xyz subject'
# content of email
email.set_content("xyz content of email")

# sending request to server
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # server object
    smtp.ehlo()

# used to send data between server and client
smtp.starttls()
# login id and password of gmail
smtp.login("email_id", "Password")
# sending email
smtp.send_message(email)

# printing success message
print("email send")