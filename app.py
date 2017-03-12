from flask import Flask
import os

import models
from resources.courses import courses_api
from resources.reviews import reviews_api

DEBUG = True
HOST = '0.0.0.0'
PORT = int(os.environ.get('PORT',5000))

app = Flask(__name__)
app.register_blueprint(courses_api,url_prefix='/api/v1')
app.register_blueprint(reviews_api,url_prefix='/api/v1')

@app.route ('/')
def hello_world():
    return 'hello'

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG,host=HOST,port=PORT)