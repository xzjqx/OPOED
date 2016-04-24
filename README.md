# OPEOD -- One Positive Energy One Day
这是一个可以挂在服务器上的Python小程序，它可以随机发送一条正能量语句到你的邮箱

## Usage
### 方法一：
首先将这个Repository Clone到你的服务器
```
git clone git@github.com:xzjqx/OPOED.git
```

然后在sentence.txt中加入你想要发送的文字，每句换行

最后修改代码
修改opeod.py中的邮箱信息
``` python
from_addr = '' #发件人邮箱
password = '' #发件人邮箱密码
to_addr = '' #收件人邮箱
#发件人邮箱可与收件人邮箱相同，即自己发给自己
smtp_server = 'smtp.qq.com' #邮箱服务器
```
按照注释填入上述信息

修改下列代码中的xxx
``` python
#发送信息
msg = MIMEText(sentence, 'plain', 'utf-8')
msg['From'] = _format_addr(u'xxx <%s>' % from_addr)
msg['To'] = _format_addr(u'xxx <%s>' % to_addr)
msg['Subject'] = Header(u'xxx', 'utf-8').encode()
```

### 方法二：
联系我：发送方法一中需要的信息到我的邮箱--xzjqx@outlook.com

## 服务器定时任务
为了让该Python程序能在服务器中定时执行，我使用cron工具
在服务器中输入一下语句
```
crontab -e
0 8 * * * python /mydata/OPEOD/opeod.py >/mydata/OPEOD/output.txt 2>&1 &
```
cron工具具体使用方法请看[初次使用crontab工具](http://www.xzjqx.me/2016/04/24/%E5%88%9D%E6%AC%A1%E4%BD%BF%E7%94%A8crontab%E5%B7%A5%E5%85%B7/)

## TODO
- 发送的信息改为每天随机十个单词
- 发送邮件改为发送短信或微信
