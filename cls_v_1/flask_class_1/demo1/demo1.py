
from flask import Flask,render_template,jsonify,request,make_response
from PIL import ImageGrab

app = Flask(__name__)
nameaddrdict={'1001':['wangwu',15,'hubei'],'1002':['zhaoliu',21,'tianjing']}
@app.route('/hello/<string:num>')
def index_f(num):
    if num in nameaddrdict:
        info=nameaddrdict[num]
        return '欢迎来到flask第一个网站%s' %info
    else:
        return 'erro'
@app.route('/user',methods=["GET"])
def user():
    return jsonify({'code':200 , 'message':'输入错误'})


@app.route('/user1',methods=['GET'])
def user2():
    args_get = request.args.get('num')
    if args_get:
        return jsonify({'code':200,'message':nameaddrdict[args_get]})

    else:
        return jsonify({'code':400,"message":"请求参数错误"})

@app.route('/user3/loggin',methods=['POST'])
def postloggin():
    user=request.form.get('username')
    passw=request.values.get('pss')
    if user and passw:
        if user in nameaddrdict :
            pasw=nameaddrdict[user]
            if passw==pasw[0]:
                return jsonify({'code':200, 'message':'loggin success'})
            else:
                return jsonify({'code':500, 'message':'password  error'})
        else:
            return 'user not register'
    else:
        return jsonify({'code': 400, 'message': 'params error'})


@app.route('/name/<string:loc>')
def getlocal(loc):

    if loc :
        if loc in nameaddrdict:
            info=nameaddrdict[loc]
            return jsonify({'loc':info})
        else:
            return jsonify({'code':400,'message':'no register'})
    else:
        return jsonify({'code':500,'message':'path fail'})

@app.route('/res')
def g():
    response=make_response('res')
    response.headers['res']='pingjiezifuchuang'
    response.set_cookie('res','nihaoa ,cookies',max_age=4000)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0' ,port=9999,debug=True)
