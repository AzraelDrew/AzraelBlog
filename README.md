## 本地部署([服务器部署](./DeployedOnTheServer.md) )

> 第一步

- 自行安装 Node14(建议使用 NVM) 与 pytohn3.8

> 第二步(安装所需的 python 库)

```shell

pip3 install django==3.2 djangorestframework django-cors-headers  Pillow requests beautifulsoup4;

```

> 第三步

```shell
# 在Django项目目录下(Blog同级目录)

mkdir upload

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser

python3 manage.py runserver

```

> 第四步

```shell
# 在azraelhtml目录下

npm i

sudo cp -r summernote-zh-CN.js ./node_modules/summernote/lang/

npm run serve
```
