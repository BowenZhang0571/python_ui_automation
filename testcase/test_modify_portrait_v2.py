"""
pytest执行测试用例-- 登录

登录用例的步骤
1、打开浏览器和网址--driver
2、点击首页的登录的link 打开登录页面
3、在登录页面里执行登录操作 -- 封装 可以直接调用

每条用例执行之前都要做浏览器初始化的操作 --前置
- 用例里调用它 得到driver  夹具【返回值】

"""
import pytest
from selenium import webdriver
from page_object.homepage_v2 import HomePage
from page_object.loginpage_v2 import LoginPage
from page_object.user_center_page import UserCenterPage
from common.handle_assert import *

@pytest.mark.skip(reason="上传用例在linux的Jenkins服务器里运行不了")
def test_modify_portrait(open_browser_url,login_avction): #调用夹具 得到返回值 drvier
    # 1、打开浏览器和网址 - -driver
    driver = open_browser_url
    # 4、点击首页个人中心
    HomePage(driver).click_usercenter_method()
    # 5、调用用户中心页面的修改头像方法
    UserCenterPage(driver).modify_portrait_method()
    # 断言 提示信息是否存在
    assert_condition(driver,UserCenterPage(driver).modify_success_tips_method())
