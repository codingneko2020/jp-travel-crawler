import requests
from bs4 import BeautifulSoup

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import smtplib
import sys

#爬最新PTT日旅板網頁
url = 'https://www.ptt.cc/bbs/Japan_Travel/index.html'
arc1 = requests.get(url)
soup = BeautifulSoup(arc1.text, 'html.parser')

title_con = soup.select(".title")
title_box = list()

for t in title_con:
    n = t.text
    print(n,end='')
    title_box.append(n)

#把資料用自己的email寄給自己
fromaddr = 'my_email'
toaddr = 'my_email'
passwd = 'my_passwd'

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = '日旅板即時文章'

body = str(title_box)
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromaddr,passwd)
text = msg.as_string()
server.sendmail(fromaddr,toaddr,text)
server.quit()

