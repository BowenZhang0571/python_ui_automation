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


class SubmitOrderPage(BasePage):
    # 商品元素
    submit_order_button_loc = (By.XPATH,'//a[text()="提交订单"]')


    # 点击添加购物车的方法
    def click_submit_button_method(self):
        logger.info("=======开始点击购物车里结算按钮操作==========")
        self.click_element(self.submit_order_button_loc)