# 맥북은 아래의 명령어를 반드시 작성한다
# ln -s /etc/ssl/* /Library/Frameworks/Python.framework/Versions/3.10/etc/openssl

import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(user_email, certification_number):
    port = 587
    smtp_server = "smtp.gmail.com"
    # 보내는 사람 이메일
    sender_email = "soyoungim.sy@gmail.com"
    # 받는 사람 이메일
    receiver_email = user_email
    # 내 구글 앱 비밀번호
    password = "urdn juds rkuh wsqk"
    message = certification_number

    msg = MIMEText(message, 'html')
    data = MIMEMultipart()
    data.attach(msg)

    context = ssl.create_default_context()
    # server = smtplib.SMTP(smtp_server, port)
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, data.as_string())