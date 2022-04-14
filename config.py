# encoding:utf-8
import os
import pymysql

DEBUG = False

SECRET_KEY = os.urandom(24)

db = pymysql.connect(host='localhost', user='root', password='1379255913zyy', db='OnlineForumPlatform', port=3306)
SQLALCHEMY_DATABASE_URI="mysql://root:1379255913zyy@localhost:3306/OnlineForumPlatform"
SQLALCHEMY_TRACK_MODIFICATIONS=False
TEMPLATES_AUTO_RELOAD =True
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = '587'
MAIL_USE_TLS = True
# MAIL_USE_SSL
MAIL_USERNAME = "422736002@qq.com"
MAIL_PASSWORD = "veuqoxwwbgqgcabh"  # 生成授权码，授权码是开启smtp服务后给出的
MAIL_DEFAULT_SENDER = "422736002@qq.com"
