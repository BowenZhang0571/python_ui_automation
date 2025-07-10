"""
登录页面： 对象 类表示
- 元素定位方法： 元组的格式 方便后面显性等待直接调用
- 元素的操作方法



"""
from time import sleep

from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.basepage_v2 import BasePage
from common.handle_path import upload_file_path


class CartPage(BasePage):
    # 商品元素
    submit_order_loc = (By.XPATH,'//a[text()="结算"]')
    # 商品选择的勾选框: 商品的名字写死的 所以最好封装方法的时候传参
    # select_checkbox_loc =(By.XPATH,'//a[contains(text(),"圆筒包")]/parent::div/preceding-sibling::div/input')

    # 购物车商品的数量
    cart_num_loc = (By.XPATH,'//span[@class="number"]')
    # 商品总价
    cart_prod_price = (By.XPATH,'//div[@class="total-price"]/span')

    # 点击添加购物车的方法
    def click_submit_order_method(self):
        logger.info("=======开始点击购物车里结算按钮操作==========")
        self.click_element(self.submit_order_loc)

    # 勾选商品CheckBox方法 -参数化
    def select_prod_checkbox_method(self,prod_name):
        logger.info("=======开始点击购物车checkbox操作==========")
        select_checkbox_loc = (By.XPATH, f'//a[contains(text(),"{prod_name}")]/parent::div/preceding-sibling::div/input')
        self.click_element(select_checkbox_loc)

    # 获取购物车商品的数量
    def get_cart_prod_num(self):
        logger.info("=======开始获取购物车商品的数量操作==========")
        cart_prod_num = self.get_text(self.cart_num_loc)
        logger.info(f"获取购物车商品的数量是：{cart_prod_num}")
        return cart_prod_num

    # 获取购物车商品的总价
    def get_cart_prod_price(self):
        logger.info("=======开始获取购物车商品的总价操作==========")
        cart_prod_price = self.get_text(self.cart_prod_price)[1:]
        logger.info(f"获取购物车商品的数量是：{cart_prod_price}")
        return cart_prod_price

    # 商品是否显示在购物车里
    def prod_dispalyed_in_cart(self,prod_name):
        logger.info("=========商品显示在购物车里检查================")
        cart_prod_name = (By.XPATH,f'//a[contains(text(),"{prod_name}")]')
        return self.element_display(cart_prod_name)
