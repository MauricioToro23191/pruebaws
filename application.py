from flask import Flask,render_template
from flask_mysqldb import MySQL

application=Flask(__name__)
application.secret_key='mysecretkey'
#configuracion de la Base de datos 
application.config['MYSQL_HOST']='us-cdbr-east-06.cleardb.net'
application.config['MYSQL_USER']='b1a740d25c64d3'
application.config['MYSQL_PASSWORD']='bfe2d3e7'
application.config['MYSQL_DB']='solvo'

db=MySQL(application)

@application.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    application.run(host="0.0.0.0",port=5000,debug=True)