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


class ProdListPage(BasePage):
    # 商品元素
    # prod_name = (By.XPATH,'//div[contains(text(),"圆筒包")]')
    # 商品名字写死了 那么用例不能灵活执行 那么名字要参数化的。


    # 判断是这个显示的方法 -- 实例方法参数化
    def prod_display_method(self,prod_name):
        logger.info("=======开始检查商品列表和页面商品是否存在==========")
        prod_name_loc = (By.XPATH, f'//div[contains(text(),"{prod_name}")]')
        return self.element_display(prod_name_loc)  # element_display的方法结果就是True或者False

    # 点击商品列表页面的元素方法
    def click_prod_method(self,prod_name):
        logger.info("=======开始点击商品列表页面商品==========")
        prod_name_loc = (By.XPATH, f'//div[contains(text(),"{prod_name}")]')
        self.click_element(prod_name_loc)