# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import re
import random

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = '' #发件人邮箱
password = '' #发件人邮箱密码
to_addr = '' #收件人邮箱
#发件人邮箱可与收件人邮箱相同，即自己发给自己
smtp_server = 'smtp.qq.com' #邮箱服务器

#随机从sentence.txt中获取一个励志句子
with open('sentence.txt', 'r') as f:
    text =  f.read()
pattern = re.compile(r'.*?\n', re.S)
match = pattern.findall(text)
num = random.randint(0, len(match)-1)
sentence = match[num]

#发送信息
msg = MIMEText(sentence, 'plain', 'utf-8')
msg['From'] = _format_addr(u'CentOS服务器 <%s>' % from_addr)
msg['To'] = _format_addr(u'xzjqx <%s>' % to_addr)
msg['Subject'] = Header(u'每日一句正能量^_^', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.ehlo()
server.starttls()
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
