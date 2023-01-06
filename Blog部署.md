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
apt install python3 libpython3.8-dev python3-venv nginx
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
pip3 install django djangorestframework django-cors-headers uwsgi Pillow requests beautifulsoup4

若uwsgi安装不成功可以使用离线安装方式
wget http://projects.unbit.it/downloads/uwsgi-latest.tar.gz
tar zxvf uwsgi-latest.tar.gz
cd uwsgi*
make
python3  setup.py install
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
chdir   =/var/www/venv/AzraelSite
module  =AzraelSite.wsgi
home    =/var/www/venv/
master  =true
processes = 4
socket  =127.0.0.1:9090
chmod-socket = 666
vacuum = true


venv表示python虚拟环境目录
socket的内容必须跟nginx.conf中uwsgi_pass一致
chdir:Django项目
module:Django项目下的wsgi
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
				listen          8000;              #端口号  记得再服务防火墙中把端口打开
				server_name     43.138.126.114;    #ip或域名
				charset         utf-8;

				location /static {
							    alias   /var/www/venv/AzraelSite/Blog/static;   #Django样式及一些静态文件

													}
				location /upload {
				          alias   /var/www/venv/AzraelSite/upload;       #用于存储图片的文件夹

													}

				location / {
							    uwsgi_pass   127.0.0.1:9090;
							    include      /etc/nginx/uwsgi_params;          #此文件必须上传
										}

				 }
	server {
        listen          80;
        server_name     43.138.126.114;
        charset         utf-8;


        location / {
                  root    /var/www/dist;    #前端代码路径
                  index   index.html ;
         						}
}
##
        # Basic Settings
        ##

        sendfile on;
        tcp_nopush on;
        tcp_nodelay on;
        keepalive_timeout 65;
        types_hash_max_size 2048;
        # server_tokens off;

        # server_names_hash_bucket_size 64;
        # server_name_in_redirect off;

        include /etc/nginx/mime.types;
        default_type application/octet-stream;

        ##
        # SSL Settings
        ##

        ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Dropping SSLv3, ref: POODLE
        ssl_prefer_server_ciphers on;

        ##
        # Logging Settings
        ##

        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;

        ##
        # Gzip Settings
        ##

        gzip on;

        # gzip_vary on;
        # gzip_proxied any;
        # gzip_comp_level 6;
        # gzip_buffers 16 8k;
        # gzip_http_version 1.1;
        # gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

        ##
        # Virtual Host Configs
        ##

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
  STATIC_ROOT='/var/www/venv/AzraelSite/Blog/static'
```

```shell
  mkdir /var/www/venv/AzraelSite/Blog/static /var/www/venv/AzraelSite/upload

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

```JavaScript
function(let a ,let b){
  console.log(a+b)
}
```

