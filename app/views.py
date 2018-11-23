import hashlib
import uuid

from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify, g

from app.exts import db
from app.models import Banners, Goods, User

blue=Blueprint('blue', __name__)

def init_blue(app):
    app.register_blueprint(blueprint=blue)

@blue.route('/')
def home():
    banners=Banners.query.all()
    goods = Goods.query.all()
    return render_template('home.html', banners=banners, goods=goods)

# 密码加密
def generate_password(password):
    hash = hashlib.md5()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest()

# 登入

@blue.route('/register/',methods=['POST','GET'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = generate_password(request.form.get('password'))
        mail = request.form.get('mail')
        # 存入数据库
        user = User()
        user.username = username
        user.password = password
        user.mail = mail
        user.token = str(uuid.uuid5(uuid.uuid4(), 'register'))
        db.session.add(user)
        db.session.commit()

        # 状态保持
        session['token'] = user.token

        return redirect(url_for('blue.home'))

    elif request.method == 'GET':
        return render_template('register.html')


# 退出
@blue.route('/quit/')
def quit():
    session.pop('token')
    return redirect(url_for('blue.home'))



# 登录
@blue.route('/login/', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = generate_password(request.form.get('password'))

        print(username)
        print(password)

        try:

            users = User.query.filter(User.username == username)
            # print(users)
            print(users.first().password)
            if users.first().password != password:
                print('1')
                return render_template('login.html', error='密码错误!!!')
            else:
                print('2')
                # response=redirect(url_for('blue.index'))
                user=users.first()
                user.token = str(uuid.uuid5(uuid.uuid4(), 'login'))
                db.session.add(user)
                db.session.commit()

                # 状态保持
                session['token'] = user.token

                return redirect(url_for('blue.home'))
        except:
            return render_template('login.html', error='用户名不存在，请重新输入')

    elif request.method == 'GET':
        return render_template('login.html')

@blue.route('/checkin/', methods=['POST','GET'])
def checkin():
    username= request.args.get('username')
    # print(pel)
    # print(type(pel))
    responseData = {
        'msg': '电话可用',
        'status': 1
    }
    # pel2=int(pel)
    # print(pel2)
    # print(type(pel2))
    users = User.query.filter(User.username==username)
    # print(users)
    # print(type(users))
    # print(users.count())
    if users.count()>0:
        # print(tels)
        responseData['msg'] = '电话已被注册'
        responseData['status'] = -1
        return jsonify(responseData)
    else:
        # print('else'+tels)
        return jsonify(responseData)

## 钩子
@blue.before_request
def before():
    token = session.get('token')
    if token:
        username = User.query.filter(User.token == token).first().username
        ls = '退出'
    else:
        username = '登录'
        ls = '注册'

    g.user = username
    g.ls = ls
