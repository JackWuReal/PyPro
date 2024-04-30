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
from selenium.webdriver.common.by import By

# # 1、打开⾕歌浏览器(实例化浏览器对象)
# driver = webdriver.Chrome()
# # 2、输⼊url
# driver.get('http://192.168.42.129/Home/user/login.html/')
# # 3、找元素及操作
# sleep(30)
# driver.quit()

"""
3.1 id定位
⽅法： driver.find_element(By.ID, 'username')
前置： 标签必须有id属性
输⼊⽅法： 元素.send_keys("内容")
"""

# 1、获取浏览器
# driver = webdriver.Chrome()
# # 2、打开url
# driver.get("http://192.168.254.131/Home/user/login.html/")
# # 3、查找操作元素
# # ⽤户名 -> id ->driver.find_element_by_id("id")
# # 元素.send_keys()输⼊⽅法
#
# driver.find_element(By.ID, 'username').send_keys("admin")
# # 密码
# driver.find_element("id","password").send_keys("123456")
# # 4、关闭浏览器
# sleep(5)
#
# driver.quit()

# 1、获取浏览器
# driver = webdriver.Chrome()
# # # 2、打开url
# driver.get("http://192.168.42.129/Home/user/login.html/")

# driver.find_element(By.NAME,'username').send_keys("admin")
# driver.find_element(By.NAME,'password').send_keys("123456")

# driver.get("http://192.168.254.131/Home/User/reg/t/email.html")
# driver.find_element(By.CLASS_NAME,"inp").send_keys("2845479857@qq.com")

# driver.get("http://192.168.254.131/Home/User/reg/t/email.html")
# driver.find_element(By.TAG_NAME,"inp").send_keys("2845479857@qq.com")
#
# driver.find_element(By.LINK_TEXT,"aaa").send_keys("2845479857@qq.com")
# driver.find_element(By.PARTIAL_LINK_TEXT,"bbbb").send_keys("2845479857@qq.com")
#
# sleep(20)
# driver.quit()

# 利用XPATH绝对位置定位
# el = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/form/div/div[1]/input")
# el.send_keys("admin")
# sleep(20)

# 利用相对位置定位
# 多个属性定位 属性之间用and 连接 、可以使用任何属性
# el = driver.find_element(By.XPATH,'//*[@type="password" and @class="text_cmu"]')
# el.send_keys("123")
# sleep(5)

# 使用层级和属性 如果元素现有的属性不能唯⼀匹配，需要结合层级使⽤
# 语法
# //⽗标签/⼦标签 必须为直属⼦级
# //⽗标签[@属性='值']//后代标签 ⽗和后代之间可以跨越元素

# 拓展
# 根据显示文本定位 //*[text()='⽂本值']
# 属性值模糊匹配： //*[contains(@属性名,'属性部分值')]

# 1、获取浏览器
driver = webdriver.Chrome()
# # 2、打开url
driver.get("http://192.168.42.129")

# 点击登录链接 ⽂本
driver.find_element(By.XPATH,"//*[text()='注册']").click()
sleep(2)

driver.find_element(By.XPATH,"//*[text()='邮箱注册']").click()
sleep(2)

# 输⼊⽤户名属性
driver.find_element(By.XPATH,"//*[@placeholder='请输入邮箱']").send_keys("13600001111")
# 密码 包含
sleep(2)

driver.find_element(By.XPATH,"//*[contains(@placeholder,'验证码') and @name='verify_code']").send_keys("CLLJ")
sleep(2)

driver.find_element(By.XPATH,"//*[contains(@placeholder,'6-16')]").send_keys("123456")
sleep(2)

driver.find_element(By.XPATH,"//*[contains(@placeholder,'再次')]").send_keys("123456")
sleep(2)

# driver.find_element(By.XPATH,"//*[text()='同意协议并注册']").click()
driver.find_element(By.XPATH,"//*[@class='clearfix checkon']/a").click()
sleep(10)

# driver.quit()

