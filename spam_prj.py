import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

email_text = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""
ref_link = 'https://dvmn.org/profession-ref-program/nikifor.business9/yNPcq/'
friend_name = 'Егор'
mailer_name = 'Никифор'
mailer_email = 'b8innabatov@yandex.ru'
friend_email = 'b8innabatov@yandex.ru'
login = os.environ.get('LOGIN')
password = os.environ.get('PASSWORD')

email_text = email_text.replace("%website%", ref_link)
email_text = email_text.replace("%friend_name%", friend_name)
email_text = email_text.replace("%my_name%", mailer_name)

letter = """\
From: {m_em}
To: {fr_em}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

{em_txt}""".format(m_em=mailer_email, fr_em=friend_email, em_txt=email_text)

letter = letter.encode('UTF-8')

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(login, password)
server.sendmail(mailer_email, friend_email, letter)
server.quit()