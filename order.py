import random

from flask import Flask, session, request, redirect, url_for, render_template, flash, Blueprint
from databank import Messages,UserInformation,Follow,OrderData,OrderMoney
from app import db2,db
import datetime
from decorators import login_limit
from page_utils import Pagination
from errors import bad_request
import time
order_api = Blueprint("order_api", __name__, url_prefix='/order_api', template_folder='templates')  # 定义模块名字为APP


def gengenerateorderID():
    re = ""
    for i in range(10):
        re += chr(random.randint(65, 90))
    return re

# 打赏
@order_api.route("/reward", methods=['POST'])
@login_limit
def reward():
    email = session.get('email')
    type1 = session.get("type")



@order_api.route("/get_orderdata", methods=['POST'])
@login_limit
def get_orderdata():
    email = request.form.get('email')
    type1 = request.form.get('type')
    id = request.form.get('id')
    if id:
        pass
    elif all([email,type1]):
        pass
    else:
        pass


#改变订单数据
@order_api.route("/change_orderdata", methods=['POST'])
@login_limit
def change_orderdata():
    list1=['False','Get','Go','True']
    id = request.form.get('id')
    ino = request.form.get('ino')
    email = request.form.get('email')
    if not all([id, ino]):
        return bad_request('missing param')
    if ino not in list1:
        return bad_request('param errors')
    try:
        cur=db.cursor()
        sql = "select ino from orderdata where id='%s'" % id
        db.ping(reconnect=True)
        cur.execute(sql)
        ino = cur.fetchone()[0]
        t = list1.index(ino)
        sql = "update orderdata set ino='%s' where id='%s'" % (list1[t + 1], id)
        db.ping(reconnect=True)
        cur.execute(sql)
        if t==1:
            sql = "update orderdata set horseman='%s' where id='%s'" % (email, id)
            db.ping(reconnect=True)
            cur.execute(sql)
            sql = "update ordermoney set horseman='%s' where id='%s'" % (email, id)
            db.ping(reconnect=True)
            cur.execute(sql)
        db.commit()
        cur.close()
        return "改变成功！"
    except Exception as e:
        raise e
