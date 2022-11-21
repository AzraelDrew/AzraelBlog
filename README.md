# AzraelBlog

> 第一步

```shell
cd azraelhtml

npm i

更换summernote的语言包
```

> 第二步

```shell
cd AzraelSite

python3 manage.py makemigrations


python3 manage.py migrate


python3 manage.py createsuperuser

mkdir upload
```

> 第三步

```shell
替换/etc/nginx/nginx.conf

server {
                                listen          80;
                                server_name     139.224.209.63;
                                index index.html
                                charset         utf-8;

                                location /static {
                                        alias   /usr/local/lib/python3.8/dist-packages/django/contrib/admin/static/;

                                }
                                location /upload {
                                        alias   /var/www/studyapi/AzraelSite/upload;

                                }

                                location / {
                                        uwsgi_pass   127.0.0.1:9090;
                                        include      /etc/nginx/uwsgi_params;
                                        client_max_body_size 20m;

                                }
}
server{
                                listen          8000;
                                server_name     139.224.209.63;
                                charset         utf-8;


                                location / {
                                        root    /var/www/study/dist;
                                        index   index.html ;
                                }

}

创建xxx.ini文件

[uwsgi]
chdir   =/var/www/studyapi/AzraelSite
module  =AzraelSite.wsgi
home    =/var/www/studyapi
master  =true
processes=4
socket  =127.0.0.1:9090
chmod-socket = 666
vacuum = true
```

> 第四步

```shell
更换 .vue和.js文件中的接口地址 以及setting.py中的url
```

> 第五步

```shell
更换summnote语言包

cd azraelhtml

sudo cp -r summernote-zh-CN.js ./node_modules/summernote/lang/
```

> Nginx

```shell
sudo service nginx start

sudo service nginx stop

sudo service nginx restart

如果安装了apache页面会变为apache的页面

#配置静态页面
sudo vim /etc/nginx/sites-available/default
```

> Django

```shell
django-admin startproject mysite

cd mysite

python3 manage.py runserver

python3 manage.py startapp myblog

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py migrate --database mysql

```

> Python 虚拟环境

```shell
python3 -m venv project

source ./project/bin/activate
```

> 数据库迁移至 mysql

```python


#在setting.py中的DATABASES的默认数据改为以下配置
        'default': {
        'ENGINE': 'django.db.backends.mysql',   #数据库引擎更改最后一个字段
        'NAME': "myblog",   #数据库名
        'USER':"root",    #用户名
        'PASSWORD':"yznaisy993279..",    #密码
        'HOST':"localhost",   #主机地址
        'PORT':"3306",    #端口
    }
```

```shell
pip install pymysql

```

```python
#直接复制在setting.py同文件夹下的__init__.py

import pymysql

pymysql.install_as_MySQLdb()

```

```shell


#迁移数据库至mysql
python3 manage.py migrate --database mysql

#重建管理员
python3 manage.py createsuperuser

```
