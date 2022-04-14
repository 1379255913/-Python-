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

user_dict1 = {}

chatroom = Blueprint("chatroom", __name__, url_prefix='/chatroom', template_folder='templates')  # 定义模块名字为APP

user_dict = {}

# 对字符串加密成整数
def encrypt(srcStr, password='1938762450'):
    # 将字符串转换成字节数组
    data = bytearray(srcStr.encode('utf-8'))
    # 把每个字节转换成数字字符串
    strList = [str(byte) for byte in data]
    # 给每个数字字符串前面加一个长度位
    strList = [str(len(s)) + s for s in strList]
    # 进行数字替换
    for index0 in range(len(strList)):
        tempStr = ""
        for index in range(len(strList[index0])):
            tempStr += password[int(strList[index0][index])]
        strList[index0] = tempStr
    return "".join(strList)

# 把整数解密成字符串
def decrypt(srcStr, password='1938762450'):
    # 数字替换还原
    tempStr = ""
    for index in range(len(srcStr)):
        tempStr += str(password.find(srcStr[index]))
    # 去掉长度位，还原成字典
    index = 0
    strList = []
    while True:
        # 取长度位
        length = int(tempStr[index])
        # 取数字字符串
        s = tempStr[index + 1:index + 1 + length]
        # 加入到列表中
        strList.append(s)
        # 增加偏移量
        index += 1 + length
        # 退出条件
        if index >= len(tempStr):
            break
    data = bytearray(len(strList))
    for i in range(len(data)):
        data[i] = int(strList[i])
    return data.decode('utf-8')

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
        inf = Messages(chatroom_name=chatroom_name,user=user_name,content=text,create_time=create_time)
        db2.session.add(inf)
        db2.session.commit()
        str1 = UserInformation.query.filter_by(email=user_name).first()
        # 返回聊天信息给前端
        emit('message', {
            'user_name': user_name,
            'text': text,
            'create_time': create_time,
            'avatar_url': str1.photo,
        }, broadcast=True)


socketio.on_namespace(MyCustomNamespace('/chatroom'))



