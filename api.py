from aiohttp import web
from config import configs
from db_driver import Driver
from views import AdsItemsV1
from views import AdsCategoriesV1
from views import UserMarkAdV1
from views import AdsValidationV1
from handlers import auth_handler_v1
from middlewares import auth_middleware_v1
from middlewares import cors_middleware_v1


async def app_factory():
	config = configs['prod']
	db = Driver(config)

	app = web.Application()

	app['db'] = db
	app['config'] = config

	# API versioning
	APIv1 = web.Application()
	APIv1.router.add_get('/auth', auth_handler_v1)
	APIv1.router.add_view('/ads_items', AdsItemsV1)
	APIv1.router.add_view('/ads_categories', AdsCategoriesV1)
	APIv1.router.add_view('/user_mark_ad', UserMarkAdV1)
	APIv1.router.add_view('/ads_validation', AdsValidationV1)
	app.add_subapp('/api/rest/v1', APIv1)

	# cors initialization
	app.middlewares.append(cors_middleware_v1)
	app.middlewares.append(auth_middleware_v1)

	return app


"""
if __name__=='__main__':
	config = configs['dev']
	db = Driver(config)

	routes = web.RouteTableDef()
	app = web.Application()

	app['db'] = db
	app['config'] = config

	# API versioning
	APIv1 = web.Application()
	APIv1.router.add_get('/auth', auth_handler_v1)
	APIv1.router.add_view('/ads_items', AdsItemsV1)
	APIv1.router.add_view('/ads_categories', AdsCategoriesV1)
	APIv1.router.add_view('/user_mark_ad', UserMarkAdV1)
	APIv1.router.add_view('/ads_validation', AdsValidationV1)
	app.add_subapp('/api/rest/v1', APIv1)

	# cors initialization
	app.middlewares.append(cors_middleware_v1)
	app.middlewares.append(auth_middleware_v1)

	if config.CONFIG_NAME == 'dev':
		web.run_app(app, port=config.PORT)
"""
