import uuid
import random

from flask_mail import Message
from flask import Flask,Blueprint,render_template,request
from page_utils import Pagination
email=Blueprint('email',__name__,url_prefix='/email',template_folder='templates/email')
from databank import Confirm
from app import db2,mail

def gengenerateID():
    re = ""
    for i in range(10):
        re += chr(random.randint(65, 90))
    return re

@email.route('/email_captcha/',methods=[ 'POST'])
def email_captcha():

    email = request.form.get('email')
    if not email:
        return "missing param"
    '''
    生成随机验证码，保存到memcache中，然后发送验证码，与用户提交的验证码对比
    '''
    captcha = str(uuid.uuid1())[:6]  # 随机生成6位验证码
    while 1:
        ID = gengenerateID()
        str2 = Confirm.query.filter_by(id=ID).first()
        if not str2: break
    inf = Confirm(id=ID,secret=captcha)
    db2.session.add(inf)
    db2.session.commit()
    #给用户提交的邮箱发送邮件
    message = Message('外卖平台邮箱验证码', recipients=[email], body='您的验证码是：%s' % captcha)
    try:
        mail.send(message)  # 发送
    except:
        return "error"
    return ID