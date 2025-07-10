"""
pytest执行测试用例-- 登录

登录用例的步骤
1、打开浏览器和网址--driver
2、点击首页的登录的link 打开登录页面
3、在登录页面里执行登录操作 -- 封装 可以直接调用

每条用例执行之前都要做浏览器初始化的操作 --前置
- 用例里调用它 得到driver  夹具【返回值】

搜索用例的断言： 判断点击搜索后的商品列表页面是否出现了这个商品元素

"""
from selenium import webdriver
from page_object.homepage_v2 import HomePage
from page_object.loginpage_v2 import LoginPage
from page_object.prod_list_page import ProdListPage
from common.handle_assert import *


def test_search_prod(open_browser_url,login_avction): #调用夹具 得到返回值 drvier
    # 1、打开浏览器和网址 - -driver
    driver = open_browser_url
    # 4、调用搜索方法
    HomePage(driver).search_prod_method("圆筒包")
    # 断言： 这个商品是显示的
    assert_condition(driver,ProdListPage(driver).prod_display_method("圆筒包"))