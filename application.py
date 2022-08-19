from flask import render_template
from init import init_app2

application,db=init_app2()

@application.route('/')
def index():
    return render_template('proto_Solvo.html')

if __name__=='__main__':
    application.run(host="0.0.0.0",port=5000,debug=True)