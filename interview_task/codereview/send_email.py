"""
Написать функцию, которая принимает json формата -
[{name: str,
email: str,
result: float
}]
И отправляет на каждый email сообщение «Привет, Артем, твой результат: 24,5»
"""

import json
import smtplib
from email.mime.text import MIMEText
from decouple import config

json_ex = """
 {"name": "Aртем",
 "email": "artemfromcodereview@gmail.com", 
 "result": 24.5}
 """


def send_email(some_json):
    data = json.loads(some_json)
    from_addr = 'somepython06@gmail.com'
    to_addr = data["email"]
    message = f'Привет, {data["name"]}, твой результат: {data["result"]}'
    msg = MIMEText(message)
    msg["Subject"] = "Поздравляю Артем!"

    username = 'somepython06'
    password = config("EMAIL_PASSWORD")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    # Выводим на консоль лог работы с сервером (для отладки)
    # server.set_debuglevel(1)
    server.starttls()

    try:
        server.login(username, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        print("The message was send successfully!")
    except Exception as _ex:
        print(f"{_ex}\n Check your login or password pls")


send_email(json_ex)

