from aiohttp import web
from aiohttp_middlewares.cors import cors_middleware
from config import configs
from db_driver import Driver
from views import AdsItemsV1
from views import AdsCategoriesV1
from views import UserMarkAdV1
from handlers import auth_handler_v1
from middlewares import auth_middleware_v1

config = configs['dev']
routes = web.RouteTableDef()
app = web.Application()
db = Driver(config)

if __name__=='__main__':
	app['db'] = db
	app['config'] = config

	# API versioning
	APIv1 = web.Application()
	APIv1.middlewares.append(auth_middleware_v1)
	APIv1.router.add_get('/auth', auth_handler_v1)
	APIv1.router.add_view('/ads_items', AdsItemsV1)
	APIv1.router.add_view('/ads_categories', AdsCategoriesV1)
	APIv1.router.add_view('/user_mark_ad', UserMarkAdV1)
	app.add_subapp('/api/rest/v1', APIv1)

	# cors initialization
	app.middlewares.append(cors_middleware())

	if config.CONFIG == 'dev':
		web.run_app(app, port=config.PORT)
