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


class UserCenterPage(BasePage):
    # 编辑资料区域
    edit_profile_text = (By.XPATH, '//div[@class="portrait-box"]')
    # 头像
    portrait_pic = (By.CLASS_NAME, 'avatar')
    # 保存账户信息
    save_info_button = (By.LINK_TEXT, '保存账户信息')
    # 修改成功的提示
    success_tips_loc = (By.CLASS_NAME, 'el-message__content')

    # 上传头像的整个方法封装
    def modify_portrait_method(self):
        logger.info("=======开始上传用户头像的操作==========")
        # 1、点击编辑资料区域
        self.click_element(self.edit_profile_text)
        # 2、点击头像
        self.click_element(self.portrait_pic)
        # 因为点击后打开windows的上传窗口有一定延迟，所以这里要等待一下再执行上传操作
        sleep(1)
        # 3、调用上传的关键字方法
        self.upload_file(upload_file_path)
        # 4、点击保存账户信息
        self.click_element(self.save_info_button)

    def modify_success_tips_method(self):
        logger.info("=======开始检查上传头像成功提示信息的操作==========")
        return self.element_display(self.success_tips_loc)