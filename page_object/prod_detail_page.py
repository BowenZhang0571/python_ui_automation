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


class ProdDetailPage(BasePage):
    # 商品元素
    add_cart_loc = (By.CLASS_NAME,"add-cart")
    # 商品名字
    prod_name_loc = (By.XPATH, '//div[@class="name-box"]/div[@class="name"]')
    # 添加购车成功提示
    add_cart_tips_loc = (By.CLASS_NAME, 'el-message__content')


    # 点击添加购物车的方法
    def click_add_cart_method(self):
        logger.info("=======开始点击商品详情页添加商品到购物车==========")
        self.click_element(self.add_cart_loc)

    # 获取商品名字方法
    def get_prod_name_method(self):
        logger.info("=========获取购物车商品名字的按钮操作================")
        return self.get_text(self.prod_name_loc)

    # 获取商品加入成功提示信息
    def get_add_cart_tips_method(self):
        logger.info("=========获取添加商品到购物车成功提示信息================")
        return self.get_text(self.add_cart_tips_loc)