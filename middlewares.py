from aiohttp import web
import jwt

@web.middleware
async def auth_middleware_v1(request, handler):
	if request.path.endswith('auth'):
		return await handler(request)

	config = request.config_dict['config']

	try:
		payload = jwt.decode(request.headers.get('Authorization', 'Bearer _').split()[1], config.SECRET_KEY, algorithms=['HS512'])
	except:
		return web.Response(status=401, text='Unauthorized')
	else:
		if payload.get('iss') == config.ISSUER:
			return await handler(request)
		else:
			return await web.Response(status=401, text='Unauthorized')
