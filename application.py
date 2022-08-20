from flask import Flask,render_template,request,jsonify
from ModelUser import ModelUser
from entities.User import User
from flask_mysqldb import MySQL

application=Flask(__name__)
application.secret_key='mysecretkey'
#configuracion de la Base de datos 
application.config['MYSQL_HOST']='us-cdbr-east-06.cleardb.net'
application.config['MYSQL_USER']='b1a740d25c64d3'
application.config['MYSQL_PASSWORD']='bfe2d3e7'
application.config['MYSQL_DB']='heroku_6d336b1af578ed7'

db=MySQL(application)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/login',methods=['GET', 'POST'])
def Hola():
    user=User(0, request.form['user'],None,None,request.form['pass'])
    R=ModelUser.login(db,user)
    return jsonify(R.__dict__)

if __name__=='__main__':
    application.run(host="0.0.0.0",port=5000,debug=True)