"""
测试数据放到py文件管理
"""
cases_all = [{'username':'','password':'lemon123456','expected':'账号为4~16位字母、数字或下划线'},
               {'username':'lemonlemonlemon11','password':'lemon123456','expected':'账号为4~16位字母、数字或下划线'},
               {'username':'lem','password':'lemon123456','expected':'账号为4~16位字母、数字或下划线'},
             {'username': 'lemon_auto', 'password': '', 'expected': '请输入密码'}]

