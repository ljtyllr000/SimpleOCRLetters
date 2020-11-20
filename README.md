环境：
    - python3、mysql、django2

### 1. 初始化
**以下为DEBUG模式**
-  修改 settings中数据库、superuser配置

**手动初始化、启动**
- db_init.py   --> 创建数据库
- python3 manage.py makemigrations
- python3 manage.py migrate
- superuser_init.py   --->  创建superuser
- python3 manage.py runserver 0.0.0.0:8000

**脚本初始化、启动**
- sudo chmod +x start.sh init.sh
- ./init.sh
- ./start.sh



### 2. 识别api

**api:**  `recognize/`

**method: ** POST

**入参：**

| 参数名      | 类型        | 必填  |      说明   |
| :-------- | :------     | :--- | ------------|
| image     | 图片文件对象  | 否    |  上传的图片  |

**返回结果：**

```json
{"status": "200", "msg": {"content": ["xxx", "yyy"]}}
或
{"status": "404", "msg": "未上传文件"}
```

