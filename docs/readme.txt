==================
djangosnippets.org
==================

2012.06.18
==========

   1. Cross-site request forgery (CSRF)

   防止恶意网站访问

   2. models.Manager

   可以认为是model admin中自定义的方法

   3. annotate,

   在QuerySet中提供一些计算函数

   Aggregation

   4. add django-debug-toolbar
   https://github.com/django-debug-toolbar/django-debug-toolbar

2012.06.16
==========

   1. 用fixture来提供初始数据

   首先在开发环境中用dumpdata命令导出指定app对应数据库中的数据，存成.json文件
      >python manage.py dumpdata cab >cab\fixtures\init_data.json

   在生产环境中，用loaddata命令导入数据
      >python manage.py loaddata cab\fixtures\init_data.json

   2. 更改首页样式

   #header #nav-main
   margin-top: 25px;

   3. 调整 base.html js，css 文件位置

   http://ajax.googleapis.com/ajax/libs/


   --ENDs