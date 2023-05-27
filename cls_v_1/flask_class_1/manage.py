
from flask import Flask

app=Flask(__name__)

class Config(object):
    DEBUG=True
    SECRET_KEY=""


app.config.from_object(Config)

@app.route('/index',methods=['GET'])
def index():
    return 'hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888)
    print('test pull')
