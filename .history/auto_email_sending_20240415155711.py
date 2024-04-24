import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_email(sender_email, sender_password, receiver_email, subject, message):
    smtp_server = "smtp.example.com"  
    smtp_port = 587  
    smtp_username = sender_email

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, sender_password)  

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server.send_message(msg)

    server.quit()

sender_email = "your_email@example.com"
sender_password = "your_password"
receiver_email = "recipient@example.com"
subject = "Test Email"
message = "This is a test email sent from Python."

send_email(sender_email, sender_password, receiver_email, subject, message)
