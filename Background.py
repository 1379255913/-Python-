from flask import Flask,Blueprint,render_template,request
from page_utils import Pagination
admin=Blueprint('admin',__name__,url_prefix='/admin',template_folder='templates/admin')
from databank import *
from app import db2
@admin.route('/')
def index():
    if request.method == 'GET':
        str1=UserInformation.query.all()
        pager_obj = Pagination(request.args.get("page", 1), len(str1), request.path, request.args,
                               per_page_count=10,
                               max_pager_count=11)
        index_list = str1[pager_obj.start:pager_obj.end]
        html = pager_obj.page_html()
        return render_template('admin_user.html',inf=index_list,html=html)

@admin.route('/shopdata')
def shopdata():
    if request.method == 'GET':
        str1 = ShopData.query.all()
        pager_obj = Pagination(request.args.get("page", 1), len(str1), request.path, request.args,
                               per_page_count=10,
                               max_pager_count=11)
        index_list = str1[pager_obj.start:pager_obj.end]
        html = pager_obj.page_html()
        return render_template('admin_shopdata.html', inf=index_list, html=html)


@admin.route('/shoptype')
def shoptype():
    if request.method == 'GET':
        str1 = ShopType.query.all()
        pager_obj = Pagination(request.args.get("page", 1), len(str1), request.path, request.args,
                               per_page_count=10,
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
                               per_page_count=10,
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
                               per_page_count=10,
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
                               per_page_count=10,
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
                               per_page_count=10,
                               max_pager_count=11)
        index_list = str1[pager_obj.start:pager_obj.end]
        html = pager_obj.page_html()
        return render_template('admin_fav.html', inf=index_list, html=html)