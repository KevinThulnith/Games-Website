from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'sararentscorps@gmail.com'
email_recever = 'kevinthulnith@gmail.com'
email_password = 'hxpdgebpzntwrkwq'

subject = 'sarents gaming'
body = """
   your verification code is 234524
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_recever
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_recever, em.as_string())