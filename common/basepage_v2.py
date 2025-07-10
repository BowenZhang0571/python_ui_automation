"""
基类-- 放每个页面都会有的一些公共的方法
 - 显性等待的方法
 - 常用操作方法

可以给到每个页面进行共享的方法

加上日志和异常捕获

"""
import time

import allure
from loguru import logger
# import pyautogui
import pyperclip
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.handle_path import screenshot_path


class BasePage:

    def __init__(self,driver):
        """初始化函数： 定义driver实例属性 在实例方法里共享"""
        self.driver = driver

    # 元素的方法  -实例方法
    def wait_element_clickable(self,locator):
        logger.info(f"等待{locator}可以被点击")
        try:
            web_element = WebDriverWait(self.driver, 8, 0.5).until(EC.element_to_be_clickable(locator))
        except Exception as e:
            logger.error(f"等待{locator}超时")
            # 发生错误 就截图-- 本地截图
            self.driver.save_screenshot(f"{screenshot_path}\screenshot_{int(time.time() * 1000)}.png")
            # allure报告里截图
            allure.attach(self.driver.get_screenshot_as_png(), name="失败用例截图",
                          attachment_type=allure.attachment_type.PNG)
            raise e
        return web_element

    def wait_element_visible(self,locator):
        logger.info(f"等待{locator}可以可见")
        # web_element代表通过显示等待找到的元素
        try:
            web_element = WebDriverWait(self.driver, 8, 0.5).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            logger.error(f"等待{locator}超时")
            # 发生错误 就截图
            self.driver.save_screenshot(f"{screenshot_path}\screenshot_{int(time.time() * 1000)}.png")
            # allure报告里截图
            allure.attach(self.driver.get_screenshot_as_png(), name="失败用例截图",
                          attachment_type=allure.attachment_type.PNG)
            raise e
        return web_element

    def wait_element_present(self, locator):
        logger.info(f"等待{locator}存在")
        # web_element代表通过显示等待找到的元素
        try:
            web_element = WebDriverWait(self.driver, 8, 0.5).until(EC.presence_of_element_located(locator))
        except Exception as e:
            logger.error(f"等待{locator}超时")
            # 发生错误 就截图
            self.driver.save_screenshot(f"{screenshot_path}\screenshot_{int(time.time() * 1000)}.png")
            # allure报告里截图
            allure.attach(self.driver.get_screenshot_as_png(), name="失败用例截图",
                          attachment_type=allure.attachment_type.PNG)
            raise e
        return web_element

    # 常用操作方法： click  send_keys js点击 鼠标点击
    # 1、上传方法
    # def upload_file(self,file_path):
    #     logger.info(f"上传文件：{file_path}")
    #     pyperclip.copy(file_path)
    #     pyautogui.hotkey("ctrl", "v")
    #     time.sleep(1)
    #     pyautogui.press('enter', presses=2)
    #     time.sleep(1)

    #2、普通点击操作--点击关键字
    def click_element(self,locator):
        logger.info(f"点击这个元素：{locator}")
        self.wait_element_clickable(locator).click()

    # 3、输入文本-关键字
    def input_text(self,locator,text):
        logger.info(f"对这个元素输入文本：{locator}，输入的内容是：{text}")
        self.wait_element_visible(locator).send_keys(text)

    # 4、获取文本
    def get_text(self,locator):
        """调用这个方法可以直接拿到这个元素的文本"""
        logger.info(f"获取这个元素的文本：{locator}")
        return self.wait_element_visible(locator).text

    # 5、获取元素的属性
    def get_attribute(self,locator,attri_name):
        """调用这个方法可以直接拿到这个元素的对应的属性"""
        logger.info(f"获取这个元素的属性：{locator}，属性是：{attri_name}")
        return self.wait_element_visible(locator).get_attribute(attri_name)

    # 6、判断元素是否可见
    def element_display(self,locator):
        """返回这个元素存在与否的布尔值：True，False"""
        logger.info(f"这个元素是否可见：{locator}")
        return self.wait_element_visible(locator).is_displayed()

    # 7、窗口切换
    def switch_window(self,page_url):
        logger.info(f"=====开始窗口切换操作==，切换的窗口是：{page_url}")
        wins = self.driver.window_handles
        for win in wins:
            if self.driver.current_url == page_url:
                break  # 如果是的我想要的页面 停止切换  跳出循环 break
            else:
                self.driver.switch_to.window(win)

    # 8、鼠标移动
    def mouse_move(self,locator):
        logger.info(f"移动鼠标到这个元素：{locator}")
        ele =  self.wait_element_present(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    # 9、鼠标点击
    def mouse_click(self,locator):
        logger.info(f"鼠标点击这个元素：{locator}")
        ele = self.wait_element_present(locator)
        ActionChains(self.driver).click(ele).perform()

    # 10、 js点击操作
    def js_click(self,locator):
        logger.info(f"js点击这个元素：{locator}")
        ele = self.wait_element_visible(locator)
        self.driver.execute_script("arguments[0].click()",ele)

    # 未完待续。。。。等以后用到了可以再进行封装 后续扩展更多关键字