class Config:
	API_KEY = 'domain'
	SECRET_KEY = 'domain'
	ISSUER = 'domain'
	CONFIG = 'dev'
	PORT = 5001
	DB_PORT = 5432
	DB_USER = 'bogdanyakupov'
	DB_PASSWORD = '3657'
	DB_HOST = 'localhost'
	DB_DBNAME = 'home'

class Dev(Config):
	pass

configs = {
	'dev': Dev
}
