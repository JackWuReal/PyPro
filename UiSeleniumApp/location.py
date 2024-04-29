# 1 通过代码调⽤⽅法查找元素

# 1、id
# 2、name
# 3、class
# 4、tag_name
# 5、link_text
# 6、partial_link_text
# 7、xpath
# 8、css
"""
1、打开⾕歌浏览器
2、输⼊url
3、找元素及操作
4、关闭浏览器
"""

from time import sleep

from selenium import webdriver

# # 1、打开⾕歌浏览器(实例化浏览器对象)
# driver = webdriver.Chrome()
# # 2、输⼊url
# driver.get('http://192.168.42.129/Home/user/login.html/')
# # 3、找元素及操作
# sleep(30)
# driver.quit()

"""
3.1 id定位
⽅法： driver.find_element_by_id("id值")
前置： 标签必须有id属性
输⼊⽅法： 元素.send_keys("内容")
"""

# 1、获取浏览器
driver = webdriver.Chrome()
# 2、打开url
driver.get("http://192.168.42.129/Home/user/login.html/")
# 3、查找操作元素
# ⽤户名 -> id ->driver.find_element_by_id("id")
# 元素.send_keys()输⼊⽅法

driver.find_element("id","username").send_keys("admin")
# 密码
driver.find_element("id","password").send_keys("123456")
# 4、关闭浏览器
sleep(5)
driver.quit()