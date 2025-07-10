"""
梳理一下下单用例完整的步骤：
前面打开浏览器和登录操作已经初始化完成--夹具里
# 搜索商品操作 ：'圆筒包'
# 商品列表页面点击商品进入商品详情页
# 进入到商品详情页-点击添加到购物车
# 点击购物车链接进入到购物车页面
# 购物车结算-勾选CheckBox
#点击结算按钮就
# 订单提交
# 进入到我的订单页面
# 关注订单的断言

"""
from time import sleep

from selenium import webdriver
from page_object.homepage_v2 import HomePage
from page_object.loginpage_v2 import LoginPage
from page_object.user_center_page import UserCenterPage
from page_object.prod_list_page import ProdListPage
from page_object.prod_detail_page import ProdDetailPage
from page_object.cart_page import CartPage
from page_object.submit_order_page import SubmitOrderPage
from page_object.my_order_page import MyOrderPage
from common.handle_assert import *


def test_modify_portrait(open_browser_url,login_avction): #调用夹具 得到返回值 drvier
    # 1、打开浏览器和网址 - -driver
    driver = open_browser_url
    # 2、搜索商品操作 ：'圆筒包'
    HomePage(driver).search_prod_method("圆筒包")
    # 3、商品列表页面点击商品进入商品详情页
    sleep(1)
    ProdListPage(driver).click_prod_method("圆筒包")
    # 4、进入到商品详情页-点击添加到购物车
    ProdDetailPage(driver).click_add_cart_method()
    # 5、点击购物车链接进入到购物车页面
    HomePage(driver).click_cart_method()
    # 6、购物车结算-勾选CheckBox
    CartPage(driver).select_prod_checkbox_method("圆筒包")
    # 7、获取购物车页面的商品价格和数量
    sleep(1)
    cart_price = CartPage(driver).get_cart_prod_price()
    cart_num = CartPage(driver).get_cart_prod_num()
    # 8、点击结算按钮就
    CartPage(driver).click_submit_order_method()
    # 9、订单提交
    SubmitOrderPage(driver).click_submit_button_method()
    # 10、点击首页里我的订单链接
    sleep(1)
    HomePage(driver).click_my_order_method()
    # 11、进入到我的订单页面-- 断言
    assert_equals(driver,MyOrderPage(driver).get_order_status_method(),"待支付")
    assert_condition(driver,"圆筒包" in MyOrderPage(driver).get_order_prodname_method())
    assert_equals(driver,MyOrderPage(driver).get_order_prod_num_method(),cart_num)
    assert_equals(driver,MyOrderPage(driver).get_order_prod_price_method(),cart_price)