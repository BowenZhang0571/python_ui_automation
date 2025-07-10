"""
做框架所有的文件的路径处理
pathlib
"""
import time
from pathlib import Path

#上传文件路径
upload_file_path = Path(__file__).parent.parent/"data"/"小柠檬.png"

# 日志路径
log_path = Path(__file__).parent.parent/"logs"/"mall_UI_auto.log"

# 报告路径
report_path = Path(__file__).parent.parent/"allure_reports"

# 截图路径处理
screenshot_path = Path(__file__).parent.parent/"screenshot"

if __name__ == '__main__':
    print(screenshot_path)
    print(f"{screenshot_path}\screenshot_{int(time.time() * 1000)}.png")