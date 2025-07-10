import time
from page_object.cart_page import CartPage
from page_object.loginpage_v2 import LoginPage
from page_object.homepage_v2 import HomePage
from page_object.prod_detail_page import ProdDetailPage
from page_object.prod_list_page import ProdListPage
from common.handle_assert import *

def test_cart(open_browser_url,login_avction):
    # 1、打开浏览器和网址 - -driver
    driver = open_browser_url
    # 2、搜索商品操作 ：'圆筒包'
    HomePage(driver).search_prod_method("圆筒包")
    # 3、商品列表页面点击商品进入商品详情页
    time.sleep(1)
    ProdListPage(driver).click_prod_method("圆筒包")
    # 4、进入到商品详情页-点击添加到购物车
    ProdDetailPage(driver).click_add_cart_method()
    cart_prod_name = ProdDetailPage(driver).get_prod_name_method()  #得到商品详情页的商品名字 用于后续断言
    # 商品详情页：断言添加购物车成功
    assert_equals(driver,ProdDetailPage(driver).get_add_cart_tips_method(),"成功加入购物车")
    # 5、点击购物车链接进入到购物车页面
    HomePage(driver).click_cart_method()
    # 断言商品名字显示在购物车里
    assert_condition(driver,CartPage(driver).prod_dispalyed_in_cart(cart_prod_name))


