DB_NAME = 'oracle'
DB_USER = 'system'
DB_PASSWORD = 'oracle'
DB_HOST = 'localhost'
DB_PORT = '1521'
DB_SERVICE = 'xe'
DIALECT='oracle'
SQL_DRIVER='cx_oracle'

ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + DB_USER + ':' + DB_PASSWORD +'@' + DB_HOST + ':' + str(DB_PORT) + '/' + DB_SERVICE

print(ENGINE_PATH_WIN_AUTH)