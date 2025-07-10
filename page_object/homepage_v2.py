"""
home页面： 对象 类表示
- 元素定位方法： 元组的格式 方便后面显性等待直接调用
- 元素的操作方法

"""
from time import sleep

from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.basepage_v2 import BasePage


class HomePage(BasePage):
    # 元素定位的表达式- 类属性
    # 登录link
    loc_login = (By.XPATH, '//a[text()="登录"]')
    # 搜索框
    search_input = (By.XPATH,'//div[@class="search-input-box"]/input')
    # 搜索的按钮
    search_button = (By.XPATH,'//div[@class="search-input-box"]/following-sibling::input')
    # 个人中心
    user_center_link = (By.XPATH, '//span[text()="个人中心"]')
    # 欢迎来到柠檬班元素
    wel_text_loc = (By.XPATH,'//span[text()="欢迎来到柠檬班"]')
    # 登录后的用户名
    uname_text_loc = (By.XPATH,'//a[@class="link-name"]')
    # 购物车元素
    cart_link_loc = (By.XPATH,'//span[@data-route="cart"]')
    # 我的订单元素
    my_order_link_loc = (By.XPATH,'//span[@data-route="order"]')

    # 点击登录link的操作方法
    def click_login_link(self):
        logger.info("=======开始点击首页的登录链接==========")
        #点击登录链接
        self.click_element(self.loc_login) #直接调用basepage里封装的关键字 --直观+代码简洁

    # 封装搜索的方法
    def search_prod_method(self,prod_name):
        logger.info("=======开始搜索商品操作==========")
        # 第一步： 输入搜索商品名字
        self.input_text(self.search_input,prod_name)
        # 第二步： 点击搜索的按钮
        self.click_element(self.search_button)

    #点击个人中心的方法
    def click_usercenter_method(self):
        logger.info("=======开始点击首页的个人中心的链接==========")
        self.click_element(self.user_center_link)

    # 点击购物车的方法
    def click_cart_method(self):
        logger.info("=======开始点击首页的购物车的链接==========")
        self.click_element(self.cart_link_loc)

    # 点击我的订单的方法
    def click_my_order_method(self):
        logger.info("=======开始点击首页的我的订单链接==========")
        self.click_element(self.my_order_link_loc)

    # 欢迎文本是否显示
    def weltext_is_display_method(self):
        logger.info("=======开始判断欢迎用户信息是否显示==========")
        return self.element_display(self.wel_text_loc)

    # 获取用户名文本
    def get_username_method(self):
        logger.info("=======开始获取登录后的用户名信息==========")
        return self.get_text(self.uname_text_loc)

