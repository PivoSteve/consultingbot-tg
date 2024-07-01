import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, from_email, password):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def format_qa_for_email(temp, userid, username):
    body = f"Вопросы и ответы от @{username} [{userid}]:\n\n"
    for item in temp:
        body += f"Вопрос {item['question']}\n\n"
        body += f"Ответ: {item['answer']}\n\n"
    return body

def send_qa_email(temp, userid, username, to_email, from_email, password):
    subject = "Ответы на вопросы бота"
    body = format_qa_for_email(temp, userid, username)
    send_email(subject, body, to_email, from_email, password)