"""
登录页面： 对象 类表示
- 元素定位方法： 元组的格式 方便后面显性等待直接调用
- 元素的操作方法

我的订单页面因为每个商品都是一样的：不好做唯一性的定位：
 - 但是需求是最新提交订单一定是在第一个显示：find_element定位结果有多个 默认获取的第一个元素。

注意订单里的商品数量+价格 是和前面购物车里勾选商品之后的数量和价格对比
 - 所以文本信息应该要一样： ×1  ￥999.00  ¥0.10  【符合中英文也会导致断言失败  所以最好只留数字】
 - 问题：如何去掉这些符号？

"""
from time import sleep

from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.basepage_v2 import BasePage
from common.handle_path import upload_file_path


class MyOrderPage(BasePage):
    # 订单的商品的名字
    order_prod_name_loc = (By.XPATH,'//a[@class="name"]')
    # 订单的商品数量
    order_prod_num_loc = (By.XPATH,'//div[@class="goods-number"]')
    # 订单的商品支付状态
    order_status_loc = (By.XPATH, '//div[@class="status"]/div')
    # 订单的价格-总价
    order_price_loc = (By.XPATH, '//div[contains(text(),"在线支付")]//span')


    # 获取订单的商品名字
    def get_order_prodname_method(self):
        logger.info("=======开始获取订单的商品名字操作==========")
        order_prod_name = self.get_text(self.order_prod_name_loc)
        logger.info(f"订单里的商品名字是：{order_prod_name}")
        return order_prod_name

    # 获取订单的数量: ×1  这个数量要去除前面x 只保留这个数字
    def get_order_prod_num_method(self):
        logger.info("=======开始获取订单的商品数量操作==========")
        order_prod_num = self.get_text(self.order_prod_num_loc)[1:]
        logger.info(f"订单里的商品名字是：{order_prod_num}")
        return order_prod_num

    # 获取订单总价: ￥999.00
    def get_order_prod_price_method(self):
        logger.info("=======开始获取订单的商品总价操作==========")
        order_price = self.get_text(self.order_price_loc)[1:]
        logger.info(f"订单里的商品名字是：{order_price}")
        return order_price

    # 获取订单支付状态: strip()默认去掉前后的空格
    def get_order_status_method(self):
        logger.info("=======开始获取订单的支付状态操作==========")
        order_status = self.get_text(self.order_status_loc).strip()
        logger.info(f"订单里的商品名字是：{order_status}")
        return order_status
