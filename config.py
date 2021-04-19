from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Ubuntu12345'
app.config['MYSQL_DATABASE_DB'] = 'bank_project'
app.config['MYSQL_DATABASE_HOST'] = '' # please use host ip for the db server
mysql.init_app(app)