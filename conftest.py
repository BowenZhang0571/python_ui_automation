"""
使用夹具 写浏览器的初始化操作
-返回driver  因为用例里需要用到这个driver

配置文件里配置的地址信息：
url = {'test':'http://mall.lemonban.com:3344/',
       'dev':'http://dev.mall.lemonban.com:3344/',
       'pre':'http://pre.mall.lemonban.com:3344/'}

get_env夹具的拿到 test dev pre 这些key，通过key取值value  得到具体测试地址。
url[get_env]

"""
import pytest
from selenium import webdriver

from page_object.homepage_v2 import HomePage
from page_object.loginpage_v2 import LoginPage
from data.setting import *
from loguru import logger
from selenium.webdriver.chrome.options import Options  # 导入无头浏览器的包


@pytest.fixture
def open_browser_url(get_env): #调用夹具就可以得到 env的值 test dev pro等值,
    # 前置： 打开浏览器和网址： 在这里调用切换浏览器的参数  ： get_env 是元组 两个数组
    env,browser = get_env # 元组解包 env=dev browser=Firefox
    # 切换浏览器：做判断 ： 如果browser的值是chrome
    # if browser.lower()=="chrome":
    #     driver = webdriver.Chrome()
    # elif browser.lower()=="firefox":
    #     driver = webdriver.Firefox()
    if browser.lower() == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")  # 解决在无头模式下可能遇到的沙箱问题
        chrome_options.add_argument("--disable-dev-shm-usage")  # 禁用/dev/shm目录用于内存文件系统
        chrome_options.add_argument("--disable-extensions")  # 禁用 GPU 加速，通常无头模式下需要
        chrome_options.add_argument("--headless")  # 启用无头模式
        chrome_options.add_argument("--start-maximized")  # 最大化窗口
        driver = webdriver.Chrome(options=chrome_options)
    elif browser.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")  # 设置火狐为headless无界面模式
        options.add_argument("--disable-gpu")
        driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    logger.info("-----初始化浏览器driver----")
    addr = url[env] #通知key取值value 的方式拿到具体的测试环境的地址
    logger.info(f"打开网址：{addr}")
    driver.get(addr)
    yield driver  # 返回driver
    # 后置: 关闭浏览器
    driver.quit()
    logger.info("-----关闭浏览器-----")

# 每一条用例执行之前都要做的登录操作 那么也可以放在夹具里
@pytest.fixture
def login_avction(open_browser_url,get_env): #夹具里可以调用夹具的
    # 1、打开浏览器和网址 - -driver
    driver = open_browser_url
    # 2、点击首页的登录的link    打开登录页面--调用HomePage的实例方法
    HomePage(driver).click_login_link()
    # 3、在登录页面里执行登录操作 - - 封装    可以直接调用-调用LoginPage的实例方法
    LoginPage(driver).login_action(username[get_env[0]], password[get_env[0]])

# 定义一个钩子函数: 如果要定义多个自定义的参数 那么在同一个钩子函数里 定义多条参数
def pytest_addoption(parser):
    # 注册自定义参数命令行参数
    parser.addoption("--env", default="test", choices=['dev', 'test', 'pre', 'prod'],
                     help="命令行参数 '--env' 设置测试环境切换")
    parser.addoption("--brow", default="chrome", choices=['chrome','firefox','safari'],
                     help="命令行参数 '--brow' 设置执行代码的浏览器")



# 定义一个夹具： 目的是为了接收pytest参数传进来的值 --这个夹具的名字可以自己随便取
@pytest.fixture()
def get_env(request):
    # option变量名就可以存储 --env的参数的值： test  dev pro
    env_value = request.config.getoption("--env")
    # 获取浏览器的参数值
    bro_value = request.config.getoption("--brow")
    logger.info(f"--env的参数的值是{env_value},--brow的参数的值{bro_value}")
    # 设置返回值 把拿到的数据返回 -- 两个参数都可以返回 别人接受的时候用元组格式保存的 (dev,firefox)
    yield env_value,bro_value