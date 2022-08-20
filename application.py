from flask import render_template,request,jsonify
from ModelUser import ModelUser
from entities.User import User
from init import init_app2

application,db=init_app2()

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/usuario/login',methods=['GET', 'POST'])
def Hola():
    user=User(0, request.form['user'],None,None,request.form['pass'])
    R=ModelUser.login(db,user)
    return jsonify(R.__dict__)

if __name__=='__main__':
    application.run(host="0.0.0.0",port=5000,debug=True)