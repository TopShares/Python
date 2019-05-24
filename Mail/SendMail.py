import smtplib
from email.header import Header  # 用来设置邮件头和邮件主题
from email.mime.text import MIMEText  # 发送正文只包含简单文本的邮件，引入MIMEText即可

def SendMail(strBody):
	# 发件人和收件人
	sender = 'nj_lbl@163.com'
	# 所使用的用来发送邮件的SMTP服务器
	smtpServer = 'smtp.163.com'
	 
	# 发送邮箱的用户名和授权码（不是登录邮箱的密码）
	username = 'nj_lbl@163.com'
	password = '9mhaoUNB'
	 
	mail_title = 'This is Title.'
	# mail_body = 'Test Body!'
	mail_body = strBody
	 
	# msg_to = ['nj_lbl@163.com,1255766369@qq.com,lb1922@gmail.com']
	msg_to = '1255877369@163.com'
	# 创建一个实例
	message = MIMEText(mail_body, 'plain', 'utf-8')  # 邮件正文
	message['From'] = sender  # 邮件上显示的发件人
	message['To'] = ','.join(msg_to)  # 邮件上显示的收件人
	message['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题
	 
	try:
		smtp = smtplib.SMTP()  # 创建一个连接
		smtp.connect(smtpServer)  # 连接发送邮件的服务器
		smtp.login(username, password)  # 登录服务器
		smtp.sendmail(sender, message['To'].split(','), message.as_string())  # 填入邮件的相关信息并发送
		print("邮件发送成功！！！")
		smtp.quit()

	except smtplib.SMTPException:
		print("邮件发送失败")
		return None

def main():
	pass

if __name__ == '__main__':
	main()