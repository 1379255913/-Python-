# encoding:utf-8
import os
import pymysql

DEBUG = False

SECRET_KEY = os.urandom(24)

db = pymysql.connect(host='localhost', user='root', password='1379255913zyy', db='OnlineForumPlatform', port=3306)
SQLALCHEMY_DATABASE_URI="mysql://root:1379255913zyy@localhost:3306/OnlineForumPlatform"
SQLALCHEMY_TRACK_MODIFICATIONS=False
