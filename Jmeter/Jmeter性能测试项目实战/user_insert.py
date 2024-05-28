# 导包
import pymysql

# 建立连接
conn = pymysql.connect(host='www.litemall360.com',port=3306,user='root',passwd='123456',db='litemall')
# 获取游标
cur = conn.cursor()

# 执行sql语句
sql1 = ("INSERT INTO `litemall`.`litemall_user` (`id`, `username`, `password`, `gender`, `birthday`, `last_login_time`, `last_login_ip`, `user_level`, `nickname`, `mobile`, `avatar`, `weixin_openid`, `session_key`, `status`, `add_time`, `update_time`, `deleted`) VALUES "
        "('{}', 'user{}', '$2a$10$lTu9qi0hr19OC800Db.eludFr0AXuJUSrMHi/iPYhKRlPFeqJxlye', 1, NULL, '2024-05-27 17:23:29', '192.168.42.1', 0, 'user{}', '{}', '', '', '', 0, '2019-04-20 22:17:43', '2024-05-27 17:23:29', 0);")

sql2 = ("INSERT INTO `litemall`.`litemall_address` (`id`, `name`, `user_id`, `province`, `city`, `county`, `address_detail`, `area_code`, `postal_code`, `tel`, `is_default`, `add_time`, `update_time`, `deleted`) VALUES "
        "('{}', 'user{}', '{}', '北京市', '市辖区', '西城区', '天通苑', '110102', '', '{}', 1, '2020-08-12 14:17:23', '2020-08-12 14:17:23', 0);")

user_start = 100000
for i in range(100000):
    user_id = user_start + i
    mobile = "13011" + str(user_id)
    addr_id = user_start + i
    print("插入第{}条数据为用户id为:{}".format(i+1,user_id))
    cur.execute(sql1.format(user_id, user_id, user_id, mobile))
    cur.execute(sql2.format(addr_id, user_id, user_id, mobile))

conn.commit() # 提交连接
# 关闭游标
cur.close()
# 关闭连接
conn.close()