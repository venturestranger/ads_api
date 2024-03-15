from aiohttp import web
from utils import build_query
from utils import headers

class AdsItemsV1(web.View):
	async def get(self):
		query = build_query('select', 'ads_items', self.request.query)
		db = self.request.config_dict['db']
		try:
			rets = await db.execute(query, fetch=True)
			for i in range(len(rets)):
				rets[i] = dict(rets[i])
		except Exception as e:
			return web.Response(status=400, text='Bad Request', headers=headers)
		else:
			return web.json_response(rets, headers=headers)
	
	async def post(self):
		data = dict(self.request.query)
		body = await self.request.json()
		data.update(body)

		query = build_query('insert', 'ads_items', data)
		db = self.request.config_dict['db']
		try:
			await db.execute(query)
		except:
			return web.Response(status=400, text='Bad Request', headers=headers)
		else:
			return web.Response(status=200, text='OK', headers=headers)
	
	async def put(self):
		data = dict(self.request.query)
		body = await self.request.json()
		data.update(body)

		query = build_query('update', 'ads_items', data)
		db = self.request.config_dict['db']
		try:
			await db.execute(query)
		except:
			return web.Response(status=400, text='Bad Request', headers=headers)
		else:
			return web.Response(status=200, text='OK', headers=headers)

	async def delete(self):
		query = build_query('delete', 'ads_items', self.request.query)
		db = self.request.config_dict['db']
		try:
			await db.execute(query)
		except:
			return web.Response(status=400, text='Bad Request', headers=headers)
		else:
			return web.Response(status=200, text='OK', headers=headers)

class AdsCategoriesV1(web.View):
	async def get(self):
		query = build_query('select', 'ads_categories', self.request.query)
		db = self.request.config_dict['db']
		try:
			rets = await db.execute(query, fetch=True)
			for i in range(len(rets)):
				rets[i] = dict(rets[i])
		except:
			return web.Response(status=400, text='Bad Request', headers=headers)
		else:
			return web.json_response(rets, headers=headers)
	
	async def post(self):
		data = dict(self.request.query)
		body = await self.request.json()
		data.update(body)

		query = build_query('insert', 'ads_categories', data)
		db = self.request.config_dict['db']
		try:
			await db.execute(query)
		except:
			return web.Response(status=400, text='Bad Request', headers=headers)
		else:
			return web.Response(status=200, text='OK', headers=headers)
	
	async def put(self):
		data = dict(self.request.query)
		body = await self.request.json()
		data.update(body)

		query = build_query('update', 'ads_categories', data)
		db = self.request.config_dict['db']
		try:
			await db.execute(query)
		except:
			return web.Response(status=400, text='Bad Request', headers=headers)
		else:
			return web.Response(status=200, text='OK', headers=headers)

	async def delete(self):
		query = build_query('delete', 'ads_categories', self.request.query)
		db = self.request.config_dict['db']
		try:
			await db.execute(query)
		except:
			return web.Response(status=400, text='Bad Request', headers=headers)
		else:
			return web.Response(status=200, text='OK', headers=headers)

class UserMarkAdV1(web.View):
	async def get(self):
		query = build_query('select', 'user_mark_ad', self.request.query)
		db = self.request.config_dict['db']
		try:
			rets = await db.execute(query, fetch=True)
			for i in range(len(rets)):
				rets[i] = dict(rets[i])
		except Exception as e:
			return web.Response(status=400, text='Bad Request', headers=headers)
		else:
			return web.json_response(rets, headers=headers)
	
	async def post(self):
		data = dict(self.request.query)
		body = await self.request.json()
		data.update(body)

		query = build_query('insert', 'user_mark_ad', data)
		db = self.request.config_dict['db']
		try:
			await db.execute(query)
		except:
			return web.Response(status=400, text='Bad Request', headers=headers)
		else:
			return web.Response(status=200, text='OK', headers=headers)
	
	async def put(self):
		data = dict(self.request.query)
		body = await self.request.json()
		data.update(body)

		query = build_query('update', 'user_mark_ad', data)
		db = self.request.config_dict['db']
		try:
			await db.execute(query)
		except:
			return web.Response(status=400, text='Bad Request', headers=headers)
		else:
			return web.Response(status=200, text='OK', headers=headers)

	async def delete(self):
		query = build_query('delete', 'user_mark_ad', self.request.query)
		db = self.request.config_dict['db']
		try:
			await db.execute(query)
		except:
			return web.Response(status=400, text='Bad Request', headers=headers)
		else:
			return web.Response(status=200, text='OK', headers=headers)
