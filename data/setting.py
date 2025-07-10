"""
保存框架配置的信息
环境的地址 测试环境、开发环境、预发布环境
test_url = 'http://mall.lemonban.com:3344/'
dev_url = 'http://dev.mall.lemonban.com:3344/'
pre_url = 'http://pre.mall.lemonban.com:3344/'
prod_url = 'http://prod.mall.lemonban.com:3344/'

环境的账号信息

代码根据执行的时候传进来的参数进行动态切换测试环境。

"""
#setting里的环境存储字典的格式：
# 环境的地址
url = {'test':'http://mall.lemonban.com:3344/',
       'dev':'http://dev.mall.lemonban.com:3344/',
       'pre':'http://pre.mall.lemonban.com:3344/'}

# 环境的账号  username["test"]--username[get_env]
username = {'test':'lemon_py',
            'dev':'lemon123',
            'pre':'lemontest'}

#环境的密码
password = {'test':'12345678',
            'dev':'lemon456',
            'pre':'lemonbest'}