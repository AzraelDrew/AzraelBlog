> 第一步

# 获取服务器的 root 权限不然会导致部署不成功

# 获取服务器的 root 权限不然会导致部署不成功

# 获取服务器的 root 权限不然会导致部署不成功

- 获取 root 方式

```shell
sudo passwd root

sudo vim /etc/ssh/sshd_config

将PermitRootLogin后面的prohibit-password改为yes

sudo reboot
```

- 安装 Nginx、python3 等环境

```shell
sudo apt install python3 nginx uwsgi libpython3.8-dev python3-venv

若uwsgi安装不成功可以使用离线安装方式
wget http://projects.unbit.it/downloads/uwsgi-latest.tar.gz
tar zxvf uwsgi-latest.tar.gz
cd uwsgi*
make
python3  setup.py install
```

- 创建 python 虚拟环境

```shell
virtualenv /var/www/vnev    #venv虚拟环境名称
```

- 启用虚拟环境

```shell
source /var/www/venv/bin/activate
```

- 安装 Django 等依赖库

```shell
pip3 install django djangorestframework django-cors-headers  Pillow requests beautifulsoup4


```

> 第二步

- 配置 uwsgi 和 nginx 分别配置 blog.ini 和 nginx.conf

```shell
#使用如下命令启动Django服务
uwsgi -d --ini  blog.ini     #-d表示再后台运行
pkill -f uwsgi -9            #杀掉uwsgi进程
```

blog.ini

```ini
[uwsgi]
chdir   = /var/www/venv/AzraelSite
module  = AzraelSite.wsgi
home    = /var/www/venv/
master  = true
processes = 4
socket  = 127.0.0.1:9090
chmod-socket = 666
vacuum = true

processes:线程数
socket:内容必须跟nginx.conf中uwsgi_pass一致
chdir:Django项目(包含manage.py的文件夹)
module:Django项目下的wsgi(包含manage.py的文件夹)
home:虚拟运行环境目录
```

nginx.conf

```
user root;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
	worker_connections 768;
	# multi_accept on;
				}
http {
					client_max_body_size 128m;
  server {
        # 端口
				listen          8000;
        # ip地址或域名
				server_name     ip address;
				charset         utf-8;

				location /static {
                  # django 后台静态文件(css)
                  alias   /var/www/venv/AzraelSite/static;
                          }
				location /upload {
                  # 上传文件夹
                  alias   /var/www/venv/AzraelSite/upload;
                          }

				location / {
                  # uwsgi_pass 必须XXX.inn文件中的socket保持一致
                  uwsgi_pass   127.0.0.1:9090;
                  include      /etc/nginx/uwsgi_params;
										}

          }
	server {
        # 端口
        listen          80;
        # ip地址或域名
        server_name     ip address;
        charset         utf-8;

        location / {
                  root    /var/www/dist;
                  index   index.html ;
                  # Vue-Router刷新页面404
                  try_files $uri $uri/ @router;
         						}
          }


        sendfile on;
        tcp_nopush on;
        tcp_nodelay on;
        keepalive_timeout 65;
        types_hash_max_size 2048;

        include /etc/nginx/mime.types;
        default_type application/octet-stream;

        ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Dropping SSLv3, ref: POODLE
        ssl_prefer_server_ciphers on;

        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;

        gzip on;

        include /etc/nginx/conf.d/*.conf;
        include /etc/nginx/sites-enabled/*;
}
#mail {
#       # See sample authentication script at:
#       # http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript
#
#       # auth_http localhost/auth.php;
#       # pop3_capabilities "TOP" "USER";
#       # imap_capabilities "IMAP4rev1" "UIDPLUS";
#
#       server {
#               listen     localhost:110;
#               protocol   pop3;
#               proxy      on;
#       }
#
#       server {
#               listen     localhost:143;
#               protocol   imap;
#               proxy      on;
#       }
#}
```

- 在 AzraelSite setting.py 中添加

```python
  STATIC_ROOT='/var/www/venv/AzraelSite/static'
```

- 创建 Django 静态文件存放目录已经上传文件目录

```shell
  mkdir /var/www/venv/AzraelSite/static /var/www/venv/AzraelSite/upload

  python3 manage.py makemigrations

  python3 manage.py migrate

  python3 manage.py createsuperuser

  python3 manage.py collectstatic
```

```shell
#使用以下命令控制nginx
service nginx restart   #重启nginx
nginx -t                #检查ngin.conf配置文件是否配置正确
```

> 第三步

- 将前端项目中的文件以及 Blog 下的 api.py 中的 127.0.0.1 替换为相应的 IP 地址
- 将前端项目打包放在 /var/www/
