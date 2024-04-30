## 定位方法

### id定位
* 方法：driver.find_element(By.ID, 'username')   
* 前置：标签必须有id属性
### name定位
* 方法：driver.find_element(By.NAME,'username')
* 前置：标签必须有name属性
* 提示：由于name属性值可以重复，所以使⽤时需要查看是否为唯⼀。
### class定位
* 方法：driver.find_element(By.CLASS_NAME,"inp").send_keys("2845479857@qq.com")
* 前置：标签必须有class属性
* 提示：由于class属性值可以有多个值,用空格隔开，默认用第一个
`如果标签有多个class值，使⽤任何⼀个都可以。如：c`
### tag name定位
* 说明：可以根据标签名进行定位
* 方法：driver.find_element(By.CLASS_NAME,"inp")
* 提示：如果⻚⾯存在多个相同标签，默认返回第⼀个。
### link text 定位
* 说明： 根据链接⽂本(a标签)定位
* ⽅法： driver.find_element(By.LINK_TEXT,"链接⽂本")

* 特点： 传⼊的链接⽂本，必须全部匹配，不能模糊
### partial_link_test 定位
* 说明： 根据链接⽂本(a标签)定位
* ⽅法： driver.find_element(By.PARTIAL_LINK_TEXT,"链接⽂本")
* 特点： 传⼊的链接⽂本，⽀持模糊匹配（传⼊局部⽂字）
