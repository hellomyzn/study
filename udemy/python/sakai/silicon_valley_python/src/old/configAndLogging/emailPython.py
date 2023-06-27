from email import message
from email.mime import multipart
from email.mime import text
import smtplib

# 送り先
smtp_host = 'smtp.live.com'
smtp_port = 587

from_email = 'xxxxx@hotmail.com'
to_email = 'em711th@icloud.com'
username = 'xxxxx@hotmail.com'
password = 'hogehoge'



"""
普通にメールを送るバージョン
msg = message.EmailMessage()
msg.set_content('Test email')
msg['Subject'] = 'Test email sube'
msg['From'] = from_email
msg['To'] =to_email
"""


msg = multipart.MIMEMultipart()
msg['Subject'] = 'Test email sube'
msg['From'] = from_email
msg['To'] =to_email
msg.attach(text.MIMEText('Test email', 'plain'))

with open('lesson.py', 'r') as f:
    attachment = text.MIMEText(f.read(), 'plain')
    attachment.add_header(
        'Content-Disposition', 'attachment', filename='lesson.txt'
    )
    msg.attachment(attachment)



server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.send_message(msg)
server.quit()
