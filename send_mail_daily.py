import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 注意，邮箱 以及接受邮箱还有邮箱验证码，应该设置在App Secret，而不是公开到仓库里面。
SENDER = os.environ.get("SENDER");
RECEIVER = os.environ.get("RECEIVER");
PASSWORD =  os.environ.get("PASSWORD");

# 邮件发送者和接收者信息
sender = SENDER  # 你的QQ邮箱 机密文件
receiver = RECEIVER  # 接收者邮箱 机密文件

# 邮件内容
subject = 'Python邮件测试'  # 邮件主题
body = '这是使用Python通过QQ邮箱发送的邮件，哈哈哈'  # 邮件正文

# 设置 SMTP 服务器及端口号
smtp_server = 'smtp.qq.com'
smtp_port = 465  # SSL端口号
password = 'your_authorization_code'  # QQ邮箱的授权码 机密文件

# 创建一个MIMEText对象，指定邮件正文内容、格式和编码
message = MIMEText(body, 'plain', 'utf-8')
message['From'] = Header(sender)
message['To'] = Header(receiver)
message['Subject'] = Header(subject)

try:
    # 连接到QQ邮箱的SMTP服务器并进行SSL加密
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    
    # 登录QQ邮箱
    server.login(sender, password)
    
    # 发送邮件
    server.sendmail(sender, [receiver], message.as_string())
    
    print("邮件发送成功")
except Exception as e:
    print(f"邮件发送失败: {e}")
finally:
    # 关闭连接
    server.quit()
