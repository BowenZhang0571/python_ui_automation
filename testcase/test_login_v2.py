"""
pytest执行测试用例-- 登录

登录用例的步骤
1、打开浏览器和网址--driver
2、点击首页的登录的link 打开登录页面
3、在登录页面里执行登录操作 -- 封装 可以直接调用

每条用例执行之前都要做浏览器初始化的操作 --前置
- 用例里调用它 得到driver  夹具【返回值】


思考：
对于用户名 和密码错误的方法 可不可以用之前登录成功的pytest方法直接使用测试？ --数据驱动
 - 不可以的  因为断言方法不一样的  要分开写
 - 数据驱动使用原则： 方法和流程是一样的，包括执行过程 和断言方法都要一样。 只是数据不一样而已 结果不一样。

是不是UI自动化永远都无法使用DDT呢？
- 也有： 如果我们用例的断言的方法可以统一写的话 那么就可以使用数据驱动。

"""
import pytest
from selenium import webdriver
from page_object.homepage_v2 import HomePage
from page_object.loginpage_v2 import LoginPage
from common.handle_assert import *
from data.setting import *

@pytest.mark.p0
def test_login(open_browser_url,get_env): #调用夹具 得到返回值 drvier
    # 1、打开浏览器和网址 - -driver
    driver = open_browser_url
    # 2、点击首页的登录的link    打开登录页面--调用HomePage的实例方法
    HomePage(driver).click_login_link()
    # 3、在登录页面里执行登录操作 - - 封装    可以直接调用-调用LoginPage的实例方法
    LoginPage(driver).login_action(username[get_env[0]],password[get_env[0]])
    # 断言操作
    # 断言1： 欢迎来到柠檬班的元素可见的
    assert_condition(driver,HomePage(driver).weltext_is_display_method())
    # 断言2： 用户名跟lemon_py文本一致
    assert_equals(driver,HomePage(driver).get_username_method(),username[get_env[0]])
    # 用户名和密码异常

# 数据驱动可以实现：测试流程 +断言方法 都是一样 满足数据驱动的条件。

#异常用例的测试数据：
from data.test_data import cases_all

@pytest.mark.parametrize("case",cases_all)
def test_login_failure(open_browser_url,case): #调用夹具 得到返回值 drvier
    # 1、打开浏览器和网址 - -driver
    driver = open_browser_url
    # 2、点击首页的登录的link    打开登录页面--调用HomePage的实例方法
    HomePage(driver).click_login_link()
    # 3、在登录页面里执行登录操作 - - 封装    可以直接调用-调用LoginPage的实例方法
    LoginPage(driver).login_action(case["username"],case["password"])
    # 断言操作
    # assert_condition(driver,LoginPage(driver).is_uname_err_display_method())
    assert_condition(driver,LoginPage(driver).is_login_err_display_method(case["expected"]))

