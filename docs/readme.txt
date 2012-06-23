==================
djangosnippets.org
==================

2012.06.23
==========

   1. SlugField

class SlugField([max_length=50, **options])
Slug is a newspaper term. A slug is a short label for something, containing only letters, numbers, underscores or hyphens.
They're generally used in URLs.

   2. signals


   3. django 多数据库
   https://docs.djangoproject.com/en/dev/topics/db/multi-db/#an-example
   http://python.dzone.com/articles/django-switching-databases?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+zones%2Fpython+%28Python+Zone%29

   4. nginx fcgi on win7

   pip install flup
   manage.py runfcgi method=threaded host=127.0.0.1 port=55880
   配置nginx.conf

        location /assets/static/ {
            alias D:\\nginx\\nginx-1.3.1\\html\\static\\;
        }

        location / {
            #root   html;
            #index  index.html index.htm;

            root   html;
            index  index.html index.htm;

            # host and port to fastcgi server
            fastcgi_pass 127.0.0.1:5588;
            fastcgi_param PATH_INFO $fastcgi_script_name;
            fastcgi_param REQUEST_METHOD $request_method;
            fastcgi_param QUERY_STRING $query_string;
            fastcgi_param SERVER_NAME $server_name;
            fastcgi_param SERVER_PORT $server_port;
            fastcgi_param SERVER_PROTOCOL $server_protocol;
            fastcgi_param CONTENT_TYPE $content_type;
            fastcgi_param CONTENT_LENGTH $content_length;
            fastcgi_pass_header Authorization;
            fastcgi_intercept_errors off;
        }

   https://code.djangoproject.com/wiki/DjangoAndNginx

   --using Gunicorn and nginx on linux

   5. solr
   http://jiaxin.im/2011/12/26/%E6%8A%98%E8%85%BE-django-solr/
   http://www.slideshare.net/simon/advanced-aspects-of-the-django-ecosystem-haystack-celery-fabric

   git clone https://github.com/screeley/solango.git


2012.06.22
==========

   1. 时间中文化
TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh-cn'

2012.06.21
==========

   1. @permalink

   cb.models.get_absolute_url

   language_list.html
      <a href="{{ language.get_absolute_url }}">{{ language.name }}</a></li>

   -- 还没体会出好处

   另一个例子:

   @permalink
   def get_absolute_url(self):
        return ('cab_snippet_detail', (), {'snippet_id': self.id})

   cab_snippet_detail --> cab.url.snippets.py :

   url(r'^(?P<snippet_id>\d+)/$',
        snippets.snippet_detail,
        name='cab_snippet_detail'),

   对应views.snippets.py
   def snippet_detail(request, snippet_id):
    return object_detail(
        request,
        queryset=Snippet.objects.all(),
        object_id=snippet_id,
        extra_context={'flag_form': SnippetFlagForm()},
    )

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