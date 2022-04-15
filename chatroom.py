import gevent
from gevent import monkey
monkey.patch_all()
import datetime
import hashlib
from flask import Flask, session, request, redirect, url_for, render_template, flash, Blueprint
from flask_socketio import emit, join_room, leave_room, Namespace
import os
from databank import Messages,UserInformation
from app import db2, socketio
from decorators import login_limit
from tools import encrypt,create_uuid
user_dict1 = {}

chatroom = Blueprint("chatroom", __name__, url_prefix='/chatroom', template_folder='templates')  # 定义模块名字为APP
basedir = os.path.abspath(os.path.dirname(__file__))
user_dict = {}




# def get_ret(s):
#     new_md5=hashlib.md5()
#     new_md5.update(s.encode('utf-8'))
#     ret=new_md5.hexdigest()
#     return ret


def judge(x,y):
    if x<y:
        return encrypt(x)+"-"+encrypt(y)
    else:
        return encrypt(y)+"-"+encrypt(x)

# 私聊
@chatroom.route("/private", methods=['POST'])
@login_limit
def private():
    user1=request.form.get('user1')
    user2=request.form.get('user2')
    if user1==user2:return redirect(url_for('index'))
    print(user1,user2)
    users=[]
    room=judge(user1,user2)
    print(room)
    str1 = UserInformation.query.filter_by(email=user1).first()
    userName=str1.nickname
    avatar_url=str1.photo
    users.append(str1)
    str2 = UserInformation.query.filter_by(email=user2).first()
    users.append(str2)
    message = Messages.query.filter(Messages.chatroom_name == room).order_by(Messages.create_time).all()
    print(message)
    return render_template("chatroom.html", userName=userName, message=message, users=users, avatar_url=avatar_url,room=str(room))


# 连接主页


class MyCustomNamespace(Namespace):
    def on_connect(self):
        print('连接成功')

    def on_joined(self, information):
        # 'joined'路由是传入一个room_name,给该websocket连接分配房间,返回一个'status'路由
        room_name = information
        user_name = session.get('email')
        print(user_name,"加入房间成功")
        join_room(room_name)
        user_dict1[user_name] = room_name
        print(user_dict1)
        emit('status', {'server_to_client': user_name + ' enter the room'}, room=room_name)

    def on_leave(self, information):
        room_name = information
        user_name = session.get('email')
        print(user_name,"退出房间成功")
        leave_room(room_name)
        user_dict1.pop(user_name)
        print(user_dict1)
        emit('status', {'server_to_client': user_name + ' leave the room'}, room=room_name)

    def on_text(self, information):
        print('接受成功')
        text = information.get('text')
        user_name = session.get('email')  # 获取用户名称
        chatroom_name = information.get('chatroom')
        create_time = datetime.datetime.now()
        create_time = datetime.datetime.strftime(create_time, '%Y-%m-%d %H:%M:%S')
        photo = information.get('photo')
        file_path = ""
        if photo:
            print("接收到了图片")
            file_path = "/static/img/" + create_uuid() + '.jpg'
            with open(basedir + file_path, 'wb+') as f:
                f.write(photo)
        inf = Messages(chatroom_name=chatroom_name,user=user_name,content=text,create_time=create_time,photo=file_path)
        db2.session.add(inf)
        db2.session.commit()
        str1 = UserInformation.query.filter_by(email=user_name).first()
        # 返回聊天信息给前端
        emit('message', {
            'user_name': str1.nickname,
            'text': text,
            'create_time': create_time,
            'photo': file_path,
            'avatar_url': str1.photo,
        }, broadcast=True)


socketio.on_namespace(MyCustomNamespace('/chatroom'))



