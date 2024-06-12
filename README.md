## flask resutful 实例

### 参考文档

- [flask-restful](https://flask-restful.readthedocs.io/en/latest/quickstart.html)
- [Flask-WTF](https://wizardforcel.gitbooks.io/flask-extension-docs/content/flask-wtf.html)
- [poetry](https://python-poetry.org/docs/cli/#config)
- [Python 进阶：With 语句和上下文管理器 ContextManager](https://zhuanlan.zhihu.com/p/24709718)
- [Python super() 详解 最简单的解释](https://www.cnblogs.com/sunzhiqi/p/16985677.html)
- [Flask 重写 wtforms 验证器异常信息](https://www.cnblogs.com/se7enjean/p/12512050.html)
- [Python 学习之 Flask 全局异常处理流程](https://blog.csdn.net/u014740628/article/details/131371242)

### TODO

- 项目初始化
- 配置文件
- 单元测试
- 参数校验
- 异常处理
- 拦截器
- 数据库
- 缓存
- 部署

### 项目初始化

- 核心初始化都放到 src/app.py 中
- 创建蓝图 ，注册蓝图
- 客户端种类非常多，注册方式很多

### 数据库

```bash
docker run -d -p 3306:3306 --name python_mysql -v /Users/liujianwei/Documents/docker_data/my_mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 mysql
```
