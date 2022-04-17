import hashlib
from flask import Flask, session, request, redirect, url_for, render_template, flash, Blueprint
from databank import Messages,UserInformation,Follow
from app import db2, socketio
import datetime
from decorators import login_limit
from page_utils import Pagination
from tools import encrypt,decrypt
messages = Blueprint("messages", __name__, url_prefix='/messages', template_folder='templates')  # 定义模块名字为APP

def get_ret(s):
    new_md5=hashlib.md5()
    new_md5.update(s.encode('utf-8'))
    ret=new_md5.hexdigest()
    return ret


@messages.route("/", methods=['GET'])
@login_limit
def messages_index():
    email = session.get("email")
    id1=encrypt(email)
    ans=[]
    str1 = Messages.query.filter(Messages.chatroom_name.like('%%%s%%' % id1)).with_entities(Messages.chatroom_name).distinct().all()
    for item in str1:
        str2=item.chatroom_name
        str3=Messages.query.filter(Messages.chatroom_name == str2).with_entities(Messages.content,Messages.create_time).order_by(Messages.create_time.desc()).first()
        str2=decrypt(str(str2).replace(id1,"").replace("-",""))
        str4=UserInformation.query.filter(UserInformation.email == str2).with_entities(UserInformation.email,UserInformation.nickname).first()
        ans.append((str4.nickname,str4.email,str3.content,str(str3.create_time)))
    pager_obj = Pagination(request.args.get("page", 1), len(ans), request.path, request.args,
                           per_page_count=10,
                           max_pager_count=11)
    index_list = ans[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    return render_template('my_messages.html', follow_list=index_list, html=html)


