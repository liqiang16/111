import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os


# 注意，邮箱 以及接受邮箱还有邮箱验证码，应该设置在App Secret，而不是公开到仓库里面。
SENDER = os.environ.get("SENDER");
RECEIVER = os.environ.get("RECEIVER");
PASSWORD =  os.environ.get("PASSWORD");

sender = SENDER  # 你的QQ邮箱 机密文件
receiver = RECEIVER  # 接收者邮箱 机密文件

subject = 'Python邮件测试'  # 邮件主题
body = '''这是使用Python通过QQ邮箱发送的邮件，哈哈哈。
测试通过，注意事项：
1 要设置repository secret 设置发件人 授权码 收件人等到 action的 repository secret
2 修改正文内容
3 rerun的时候 要新建一个job 不能一直re-run 那个failed job。
'''  # 邮件正文

# 设置 SMTP 服务器及端口号
smtp_server = 'smtp.qq.com'
smtp_port = 587
password = PASSWORD  # QQ邮箱的授权码 机密文件

# 创建一个MIMEText对象，指定邮件正文内容、格式和编码
message = MIMEText(body, 'plain', 'utf-8')
message['From'] = Header(sender)
message['To'] = Header(receiver)
message['Subject'] = Header(subject)

try:
    # 连接到QQ邮箱的SMTP服务器并进行SSL加密
    server = smtplib.SMTP(smtp_server, smtp_port, timeout=10)
    # 启动 TLS 安全连接
    server.starttls()
    # 登录QQ邮箱
    server.login(sender, password)
    # 发送邮件
    server.sendmail(sender, [receiver], message.as_string())
    
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(f"邮件发送失败: {e}")
except Exception as e:
    print(f"其他错误: {e}")
finally:
    # 关闭连接
    try:
        server.quit()
    except:
        pass