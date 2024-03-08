import asyncpg as db
from utils import log

class Driver:
	def __init__(self, config):
		self.user = config.DB_USER
		self.password = config.DB_PASSWORD
		self.host = config.DB_HOST
		self.database = config.DB_DBNAME
	
	async def init(self):
		pass

	async def execute(self, query, fetch=False):
		try:
			conn = await db.connect(user=self.user, password=self.password, host=self.host, database=self.database)
			rows = await conn.execute(query)
			if fetch == True:
				rows = await conn.fetch(query)
				return rows
		except Exception as e:
			log('DB Driver ERROR: ' + str(e))
			raise Exception()
		finally:
			await conn.close()
