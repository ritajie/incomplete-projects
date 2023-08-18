# 烂尾、停贷楼盘 的数据汇总

已上线：~~https://building.lulaolu.com~~ (被请喝茶了，网站已下线)

这个项目的目标是：统计`烂尾楼盘`和`停贷楼盘`。现在只统计了停贷楼盘，后续会补充更多数据。

![alt text](https://github.com/ritajie/incomplete-projects/blob/master/incomplete_projects/static/img/demo.png?raw=true)



## 数据从哪里来？
* 停贷楼盘：[GitHub - WeNeedHome](https://github.com/WeNeedHome/SummaryOfLoanSuspension)
* 烂尾楼盘：[人民网 - 领导留言板 - 住房和城乡建设部](http://liuyan.people.com.cn/threads/list?fid=5063&position=1)

这是我整理的结构化数据（JSON）
[📃 github_building_and_amap_building.json](https://github.com/ritajie/incomplete-projects/blob/master/incomplete_projects/config/github_building_and_amap_building.json)

## 后续工作
* 持续更新停贷数据
* 根据人民网的留言板，写一个词法分析（或者索性人工分析），找到业主投诉停工的楼盘，尽可能及时得更新烂尾数据。

欢迎大家一起来共享数据和代码！

这个世界会好的。

## 在本地开发

0. 不要使用主分支，请进入 `before-offline` 分支

    ```bash
    git checkout before-offline
    ```

1. 安装依赖

    ```bash
    # Python 3.6+
    python -m venv venv && source venv/bin/activate
    pip install -r requirements.txt
    ```

2. 配置 config.py

    ```bash
    DB_NAME=...
    DB_USER=...
    DB_PASSWORD=...
    DB_HOST=...
    DB_PORT=...

    CONFIG_PATH=incomplete_projects/config/config.py
    touch $CONFIG_PATH
    echo database_name = "'$DB_NAME'" >> $CONFIG_PATH
    echo database_user = "'$DB_USER'" >> $CONFIG_PATH
    echo database_password = "'$DB_PASSWORD'" >> $CONFIG_PATH
    echo database_host = "'$DB_HOST'" >> $CONFIG_PATH
    echo database_port = $DB_PORT >> $CONFIG_PATH
    echo django_secret_key = "'just-some-random-string'" >> $CONFIG_PATH
    ```

3. 初始化数据库

    ```sql
    -- 登录数据库: mysql -u $DB_USER -p$DB_PASSWORD -h $DB_HOST -P $DB_PORT
    MySQL > CREATE DATABASE IF NOT EXISTS `building`;
    MySQL > use `building`;
    MySQL > source backup_db.sql;
    ```

4. 启动服务（开发模式）

    ```bash
    python manage.py runserver
    ```