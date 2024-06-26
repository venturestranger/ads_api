from aiohttp import web
from utils import headers
import jwt

@web.middleware
async def cors_middleware_v1(request, handler):
	if request.method == 'OPTIONS':
		return web.Response(status=200, text='OK', headers=headers)
	else:
		return await handler(request)

@web.middleware
async def auth_middleware_v1(request, handler):
	
	if request.path.endswith('auth'):
		return await handler(request)

	config = request.config_dict['config']

	try:
		payload = jwt.decode(request.headers.get('Authorization', 'Bearer _').split()[1], config.SECRET_KEY, algorithms=['HS512'])
	except Exception as e:
		return web.Response(status=401, text='Unauthorized', headers=headers)
	else:
		if payload.get('iss') == config.ISSUER:
			return await handler(request)
		else:
			return web.Response(status=401, text='Unauthorized', headers=headers)
