""""
from flask.ext.mysqldb import MySQL
import sys
# Open database connection
db = MySQLdb.connect("localhost","root","2197832","sakonwaba" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT * FROM 'products'")

# Fetch a single row using fetchone() method.
data = cursor.fetchall()

for row in data:
	print row[0]


#print "Database version : %s " % data
cursor.close()
# disconnect from server
db.close()   

sys.exit()

"""""


from flask import Flask
from flask.ext.mysqldb import MySQL




app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '2197832'
app.config['MYSQL_DB'] = 'sakonwaba'

@app.route('/')
def sakonwaba():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products")
    rv = cur.fetchall()
    return str(rv)

if __name__ == '__main__':
    app.run(debug=True)