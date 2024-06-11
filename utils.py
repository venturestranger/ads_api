# Headers for responses
headers = {
	"Access-Control-Allow-Origin": "*",
	"Access-Control-Allow-Methods": "*",
	"Access-Control-Allow-Headers": "*",
	"Access-Control-Max-Age": "86400"
}


# A logging module
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

def log(msg, status='error'):
	if status == 'info':
		logger.info(msg)
	else:
		logger.error(msg)


# Query sanitizer
def sanitize(dct: dict) -> dict:
	data = {}
	prune = lambda x: re.sub(r"[^a-zа-яA-ZА-Я0-1\_\ ]+", '', x)

	for key, item in dct.items():
		data.update({prune(key): prune(item)})

	return data

# Query builder
def build_query(query_type, table, query):
	query = sanitize(query)

	spec = ['order_by_', 'order_way_', 'limit_', 'offset_']
	aggr = ['key_', 'func_']

	prefix = ''
	suffix = ''

	match query_type:
		case 'select':
			if query.get('func_', None) == None:
				prefix = f'SELECT * FROM {table} '
			else:
				prefix = f"SELECT {query['func_']}({query.get('key_', 'id')}) FROM {table} WHERE "
		case 'update':
			prefix = f'UPDATE {table} SET '
			suffix = ' WHERE '
		case 'delete':
			prefix = f'DELETE FROM {table} WHERE '
		case 'insert':
			prefix = f'INSERT INTO {table}('
			suffix = ') VALUES('
	
	if query_type == 'update':
		tf = False
		for key, value in query.items():
			if not key in spec and not key in aggr and key != 'id':
				if tf:
					prefix += ', '
				prefix += f" {key} = '{value}' "
				tf = True
		suffix += f" id = '{query.get('id')}'"
	elif query_type == 'delete':
		tf = False
		for key, value in query.items():
			if not key in spec and not key in aggr:
				if tf:
					prefix += ' AND '
				prefix += f" {key} = '{value}' "
				tf = True
	elif query_type == 'select':
		tf = False
		for key, value in query.items():
			if not key in spec and not key in aggr:
				if tf:
					prefix += ' AND '
				else:
					prefix += ' WHERE '
				prefix += f" {key} = '{value}' "
				tf = True
			elif not key in aggr:
				if key == 'order_way_':
					suffix += f" {value} "
				else:
					suffix += f" {key[:-1].replace('_', ' ')} {value} "
	else:
		prefs = []
		sufs = []
		for key, value in query.items():
			if not key in spec and not key in aggr:
				prefs.append(f"{key}")
				sufs.append(f"'{value}'")

		prefix += ', '.join(prefs)
		suffix += ', '.join(sufs) + ')'

	print(prefix + suffix)
	return prefix + suffix

if __name__=="__main__":
	query = {
		'id': 1,
		'name': 'Bogdan',
		'meta': 'hell',
		'order_by_': 'id',
		'order_way_': 'asc',
		'limit_': 3,
		'offset_': 1,
		'key_': 'id',
		'func_': 'max'
	}

	log(build_query('insert', 'ads', query))
	log(build_query('delete', 'ads', query))
	log(build_query('update', 'ads', query))
	log(build_query('select', 'ads', query))
