import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os 
# 使用免费 serv00 企业邮箱 也能正常发送

# 注意，邮箱 以及接受邮箱还有邮箱验证码，应该设置在App Secret，而不是公开到仓库里面。
SENDER = 'abc@demo.serv00.com'
RECEIVER = 'a123@demo.serv00.com'; 
PASSWORD =  'passwordxxx';


sender = SENDER
receiver = RECEIVER

subject = 'Python邮件测试'
body = '这是使用Python通过Sev00邮箱发送的邮件，哈哈哈'

# 设置 SMTP 服务器及端口号
smtp_server = 'mail7.serv00.com'
smtp_port = 465
password = PASSWORD

message = MIMEText(body, 'plain', 'utf-8')
message['From'] = Header(sender)
message['To'] = Header(receiver)
message['Subject'] = Header(subject)

try:
    # use SMTP_SSL directly
    server = smtplib.SMTP_SSL(smtp_server, smtp_port, timeout=10)
    server.login(sender, password)
    server.sendmail(sender, [receiver], message.as_string())
    
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(f"邮件发送失败: {e}")
except Exception as e:
    print(f"其他错误: {e}")
finally:
    try:
        server.quit()
    except:
        pass