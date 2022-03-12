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
