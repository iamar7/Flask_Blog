
class Config:
	SECRET_KEY = '09a780d6915386d98f7316e396267836'
	SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
	MAIL_SERVER ='smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = '@gmail.com' #Put some mail id & pass 
	MAIL_PASSWORD = '' #and allow less secure apps in google settings