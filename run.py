"""
收集和执行所有的测试用例
- 写日志文件
- 生成测试报告


需求： 希望在Jenkins-- 命令行模式运行的时候 也可以在命令行后面添加参数 选择你要执行的环境和浏览器。
python run.y test firefox

cmd或者terminal里执行的话 执行命令后面可以跟上参数的 但是这个参数需要用代码接受一下才可以。
- 借助自带的库 sys： sys.argv
- 可以接受命令传过来的所有的参数：列表进行保存  ['.\\run.py', 'test', 'firefox'] 拿哪个参数进行索引取值。
 - test： sys.argv[1]
 - firefox:sys.argv[2]
目的：为了拿到命令行的参数 放在pytest.mian调用，然后去执行和使用。

"""
from loguru import logger
import pytest
from common.handle_path import log_path,report_path
import sys


#写入日志文件
logger.add(sink=log_path,
           encoding="UTF8",
           level="INFO",
           rotation="20MB",
           retention="1 day")


# 使用讴歌sys.argv 接受命令传过来的参数
print(sys.argv)
# 因为如果没有传参数 这个里取值索引溢出报错了 所以可以做个异常捕获：如果异常了设置一个默认值 代码不会报错
try:
    scrip,env_para,bro_para = sys.argv
except Exception as e:
    env_para="test"
    bro_para="chrome"

# 执行并生成测试报告
# pytest.main(["-v","-s",f"--alluredir={report_path}","--clean-alluredir",
#              "-m p0","--reruns","2","--reruns-delay","5"])
# pytest.main(["-v","-s",f"--alluredir={report_path}","--clean-alluredir",
#            "-m p0",f"--env={env_para}",f"--brow={bro_para}"])

pytest.main(["-v","-s",f"--alluredir={report_path}","--clean-alluredir",
    f"--env={env_para}",f"--brow={bro_para}"])