"""
封装断言方法做封装：
- 加日志
- 加异常捕获
- 后面直接调用断言的方法

目前用到的是
 - 断言条件成立的
 - 断言预期结果 == 实际结果
 可能还会有其他的断言  后面可以再丰富和扩展的。

"""
import time

import allure
from loguru import logger


from common.handle_path import screenshot_path

#  - 断言预期结果 == 实际结果
def assert_equals(driver,actual,expected):
    logger.info("===========开始做断言： 预期结果是否等于执行结果============")
    try:
        assert actual==expected
        logger.info(f"断言成功！预期结果是：【{expected}】，实际结果是：【{actual}】")
    except AssertionError as e:
        logger.error(f"断言失败了！预期结果是：【{expected}】，实际结果是：【{actual}】")
        # 发生错误 就截图
        driver.save_screenshot(f"{screenshot_path}\screenshot_{int(time.time() * 1000)}.png")
        # allure报告里截图
        allure.attach(driver.get_screenshot_as_png(), name="失败用例截图",
                      attachment_type=allure.attachment_type.PNG)
        raise e

#  - 断言条件成立的
def assert_condition(driver,condition):
    logger.info("===========开始做断言：条件是否成立============")
    try:
        assert condition
        logger.info(f"断言成功！条件【{condition}】成立的！")
    except AssertionError as e:
        logger.error(f"断言失败了！条件【{condition}】不成立的！")
        # 发生错误 就截图
        driver.save_screenshot(f"{screenshot_path}\screenshot_{int(time.time() * 1000)}.png")
        # allure报告里截图
        allure.attach(driver.get_screenshot_as_png(), name="失败用例截图",
                      attachment_type=allure.attachment_type.PNG)
        raise e