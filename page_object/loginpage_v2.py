"""
登录页面： 对象 类表示
- 元素定位方法： 元组的格式 方便后面显性等待直接调用
- 元素的操作方法

所以这个用户和密码错误tips信息那条用例不可以一起做DDT  单独写一条测试用例。

"""
from time import sleep

from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.basepage_v2 import BasePage


class LoginPage(BasePage):
    # 元素定位的表达式- 类属性
    # 用户名输入框
    loc_username = (By.XPATH, '//input[@placeholder="请输入手机号/用户名"]')
    # 密码输入框
    loc_password = (By.XPATH, '//input[@placeholder="请输入密码"]')
    # 登录按钮
    loc_login_but = (By.CLASS_NAME, 'login-button')
    # 用户名输入错误或为空的错误提示信息
    # uname_err_tips_loc = (By.XPATH,'//div[text()="账号为4~16位字母、数字或下划线"]')
    # # 用户名输入错误或为空的错误提示信息
    # passwd_err_tips_loc = (By.XPATH,'//div[text()="请输入密码"]')



    # 登录操作方法
    def login_action(self,uname,passwd):
        logger.info("=======开始做登录操作==========")
        # 输入用户名
        self.input_text(self.loc_username,uname)
        # 输入密码
        self.input_text(self.loc_password, passwd)
        # 点击登录按钮
        self.click_element(self.loc_login_but)
        # 登录之后加一个强制等待
        sleep(1)

    # 判断错误提示是否存在
    # def is_uname_err_display_method(self):
    #     logger.info("=======开始判断用户名错误的提示信息存在操作==========")
    #     return self.element_display(self.uname_err_tips_loc)

    # 判断错误提示是否存在
    # def is_passwd_err_display_method(self):
    #     logger.info("=======开始判断密码错误的提示信息存在操作==========")
    #     return self.element_display(self.passwd_err_tips_loc)

    # 如果可以把这两个断言的方法统一为一个， 这两条用例可以用同一个断言方法实现 那么就可以用DDT。
    def is_login_err_display_method(self,err_info):
        logger.info("=======开始判断登录错误的提示信息存在操作==========")
        err_loc = (By.XPATH, f'//div[text()="{err_info}"]')
        return self.element_display(err_loc)