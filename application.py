from flask import Flask,render_template
from flask_cors import CORS
from init import init_app2

application,db=init_app2()
CORS(application)

@application.route('/')
def index():
    return render_template('proto_Solvo.html')

if __name__=='__main__':
    application.run(host="0.0.0.0",port=80,debug=True)