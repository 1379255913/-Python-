"""
# # 在线查看文件
# @app.route('/online_file/<Fno>')
# def online_file(Fno):
#     return send_from_directory(os.path.join('store'), Fno)
#
#
# # 文件下载功能
# @app.route('/download/<Fno>')
# def download(Fno):
#     return send_file(os.path.join('store') + "/" + Fno, as_attachment=True)
# # 资源上传页面
# @app.route('/post_file', methods=['GET', 'POST'])
# @login_limit
# def post_file():
#     if request.method == 'GET':
#         return render_template('post_file.html')
#     if request.method == 'POST':
#         email = session.get('email')
#         upload_file = request.files.get('file')
#         filename = request.form.get('filename')
#         file_info = request.form.get('file_info')
#         file_path = 'store'
#         file_time = time.strftime("%Y-%m-%d %H:%M:%S")
#         Fno = gengenerateFno()
#         try:
#             cur = db.cursor()
#             sql = "select * from Files where Fno = '%s'" % Fno
#             db.ping(reconnect=True)
#             cur.execute(sql)
#             result = cur.fetchone()
#             # 如果result不为空，即该Fno已存在时，一直生成随机的Fno，只到该数据库中不存在
#             while result is not None:
#                 Fno = gengenerateFno()
#                 sql = "select * from Files where Fno = '%s'" % Fno
#                 db.ping(reconnect=True)
#                 cur.execute(sql)
#                 result = cur.fetchone()
#             # 获取文件的后缀
#             upload_name = str(upload_file.filename)
#             houzhui = upload_name.split('.')[-1]
#             # 保存在本地的名字为生成的Fno+文件后缀，同时修改Fno的值
#             Fno = Fno + "." + houzhui
#             # 保存文件到我们的服务器中
#             upload_file.save(os.path.join(file_path, Fno))
#             # 将文件信息存储到数据库中
#             sql = "insert into Files(Fno, filename, file_info, file_time,email) VALUES ('%s','%s','%s','%s','%s')" % (
#             Fno, filename, file_info, file_time, email)
#             db.ping(reconnect=True)
#             cur.execute(sql)
#             db.commit()
#             cur.close()
#             return redirect(url_for('source'))
#         except Exception as e:
#             raise e
#
#
# # 资源专区
# @app.route('/source')
# def source():
#     if request.method == 'GET':
#         try:
#             cur = db.cursor()
#             sql = "select Fno,filename,file_info,file_time,nickname from Files,UserInformation where Files.email = UserInformation.email"
#             db.ping(reconnect=True)
#             cur.execute(sql)
#             files = cur.fetchall()
#             cur.close()
#             return render_template('source.html', files=files)
#         except Exception as e:
#             raise e
"""