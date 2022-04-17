from flask import Flask,Blueprint,render_template,request
from page_utils import Pagination
admin=Blueprint('admin',__name__,url_prefix='/admin',template_folder='templates/admin')
from databank import *
from app import db2
@admin.route('/')
@admin.route('/user')
def index():
    if request.method == 'GET':
        str1=UserInformation.query.all()
        pager_obj = Pagination(request.args.get("page", 1), len(str1), request.path, request.args,
                               per_page_count=20,
                               max_pager_count=11)
        index_list = str1[pager_obj.start:pager_obj.end]
        html = pager_obj.page_html()
        return render_template('admin_user.html',inf=index_list,html=html)

@admin.route('/shopdata')
def shopdata():
    if request.method == 'GET':
        str1 = ShopData.query.all()
        pager_obj = Pagination(request.args.get("page", 1), len(str1), request.path, request.args,
                               per_page_count=20,
                               max_pager_count=11)
        index_list = str1[pager_obj.start:pager_obj.end]
        html = pager_obj.page_html()
        return render_template('admin_shopdata.html', inf=index_list, html=html)


@admin.route('/shoptype')
def shoptype():
    if request.method == 'GET':
        str1 = ShopType.query.all()
        pager_obj = Pagination(request.args.get("page", 1), len(str1), request.path, request.args,
                               per_page_count=20,
                               max_pager_count=11)
        index_list = str1[pager_obj.start:pager_obj.end]
        html = pager_obj.page_html()
        return render_template('admin_shoptype.html', inf=index_list, html=html)


@admin.route('/orderdata')
def orderdata():
    if request.method == 'GET':
        str1 = OrderData.query.all()
        for j in str1:
            str2=UserInformation.query.filter_by(email=j.email).first()
            j.nickname_user=str2.nickname
            str2 = UserInformation.query.filter_by(email=j.shop).first()
            j.nickname_shop = str2.nickname
            str2 = UserInformation.query.filter_by(email=j.horseman).first()
            if str2:
                j.nickname_horseman = str2.nickname
            else:j.nickname_horseman=""
        pager_obj = Pagination(request.args.get("page", 1), len(str1), request.path, request.args,
                               per_page_count=20,
                               max_pager_count=11)
        index_list = str1[pager_obj.start:pager_obj.end]
        html = pager_obj.page_html()
        return render_template('admin_orderdata.html', inf=index_list, html=html)


@admin.route('/ordermoney')
def ordermoney():
    if request.method == 'GET':
        str1 = OrderMoney.query.all()
        for j in str1:
            str2=UserInformation.query.filter_by(email=j.email).first()
            j.nickname_user=str2.nickname
            str2 = UserInformation.query.filter_by(email=j.shop).first()
            j.nickname_shop = str2.nickname
            str2 = UserInformation.query.filter_by(email=j.horseman).first()
            if str2:
                j.nickname_horseman = str2.nickname
            else:j.nickname_horseman=""
        pager_obj = Pagination(request.args.get("page", 1), len(str1), request.path, request.args,
                               per_page_count=20,
                               max_pager_count=11)
        index_list = str1[pager_obj.start:pager_obj.end]
        html = pager_obj.page_html()
        return render_template('admin_ordermoney.html', inf=index_list, html=html)


@admin.route('/likes')
def likes():
    if request.method == 'GET':
        str1 = Likes.query.all()
        for j in str1:
            str2=UserInformation.query.filter_by(email=j.email).first()
            j.nickname_user=str2.nickname
            str2 = UserInformation.query.filter_by(email=j.shop_email).first()
            j.nickname_shop = str2.nickname
        pager_obj = Pagination(request.args.get("page", 1), len(str1), request.path, request.args,
                               per_page_count=20,
                               max_pager_count=11)
        index_list = str1[pager_obj.start:pager_obj.end]
        html = pager_obj.page_html()
        return render_template('admin_likes.html', inf=index_list, html=html)


@admin.route('/fav')
def fav():
    if request.method == 'GET':
        str1 = Fav.query.all()
        for j in str1:
            str2=UserInformation.query.filter_by(email=j.email).first()
            j.nickname_user=str2.nickname
            str2 = UserInformation.query.filter_by(email=j.shop_email).first()
            j.nickname_shop = str2.nickname
        pager_obj = Pagination(request.args.get("page", 1), len(str1), request.path, request.args,
                               per_page_count=20,
                               max_pager_count=11)
        index_list = str1[pager_obj.start:pager_obj.end]
        html = pager_obj.page_html()
        return render_template('admin_fav.html', inf=index_list, html=html)


@admin.route('/follow')
def follow():
    if request.method == 'GET':
        str1 = Follow.query.all()
        for j in str1:
            str2=UserInformation.query.filter_by(email=j.email).first()
            j.nickname_user=str2.nickname
            str2 = UserInformation.query.filter_by(email=j.follow_email).first()
            j.nickname_followed = str2.nickname
        pager_obj = Pagination(request.args.get("page", 1), len(str1), request.path, request.args,
                               per_page_count=20,
                               max_pager_count=11)
        index_list = str1[pager_obj.start:pager_obj.end]
        html = pager_obj.page_html()
        return render_template('admin_follow.html', inf=index_list, html=html)

@admin.route('/issue')
def issue():
    if request.method == 'GET':
        str1 = Issue.query.all()
        for j in str1:
            j.Ino2=j.Ino[:30]
            str2 = UserInformation.query.filter_by(email=j.email).first()
            j.nickname_user = str2.nickname
            str2 = UserInformation.query.filter_by(email=j.shop).first()
            j.nickname_shop = str2.nickname
        pager_obj = Pagination(request.args.get("page", 1), len(str1), request.path, request.args,
                               per_page_count=20,
                               max_pager_count=11)
        index_list = str1[pager_obj.start:pager_obj.end]
        html = pager_obj.page_html()
        return render_template('admin_issue.html', inf=index_list, html=html)

@admin.route('/ans/<Ino>')
def ans(Ino):
    if request.method == 'GET':
        return Ino

@admin.route('/comment')
def comment():
    if request.method == 'GET':
        str1 = Comment.query.all()
        for j in str1:
            j.Ino2=j.Ino[:30]
            str2 = UserInformation.query.filter_by(email=j.email).first()
            j.nickname_user = str2.nickname
        pager_obj = Pagination(request.args.get("page", 1), len(str1), request.path, request.args,
                               per_page_count=20,
                               max_pager_count=11)
        index_list = str1[pager_obj.start:pager_obj.end]
        html = pager_obj.page_html()
        return render_template('admin_comment.html', inf=index_list, html=html)

@admin.route('/comment_detail', methods=['POST'])
def comment_detail():
    if request.method == 'POST':
        id=request.form.get("id")
        str1 = Comment.query.filter_by(id=id).first()
        return render_template('admin_comment_detail.html',inf=str1)


# 权限操作
@admin.route('/right/<Ino>', methods=['GET'])
def right(Ino):
    if request.method == 'GET':
        inf = db2.session.query(Ban).filter(Ban.email == Ino).first()
        inf2 = db2.session.query(UserInformation).filter(UserInformation.email == Ino).first()
        return render_template('admin_right.html', inf=inf ,inf2=inf2)


# 禁言
@admin.route('/ban_api', methods=['POST'])
def ban_api():
    email = request.form.get('email')
    value = request.form.get('value')
    flag = 'True'

    inf = db2.session.query(Ban).filter(Ban.email == email).first()
    if not inf:
        inf2=""
        if value=='comment':
            inf2 = Ban(email=email,comment=True)
        db2.session.add(inf2)
    else:
        if inf.comment:
            inf.comment=""
            flag = 'False'
        else:
            inf.comment="True"
    db2.session.commit()
    return  flag