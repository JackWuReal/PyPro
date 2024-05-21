import pymysql

conn = pymysql.connect(host='www.litemall360.com', user="root",password="123456",database="litemall",port=3306,charset='utf8')

cursor = conn.cursor()

addr_sql = ("INSERT INTO `litemall`.`litemall_address` (`id`, `name`, `user_id`, `province`, `city`, `county`, `address_detail`, `area_code`, `postal_code`, `tel`, `is_default`, `add_time`, `update_time`, `deleted`) "
            "VALUES ('{}', '{}', '{}', '北京市', '市辖区', '西城区', '天通苑', '110102', '', '{}', '1', '2020-08-12 14:17:23', '2020-08-12 14:17:23', '0');")

user_start =100000
for i in range(100000):
    addr_id = user_start + i
    user_id = user_start + i
    username = "test"+str(user_id)
    mobile = "13012"+str(user_id)

    print("插入第{}条数据ID为{}".format(i+1,user_id))
    sql = addr_sql.format(addr_id,username,user_id,mobile)
    cursor.execute(sql)
    conn.commit()
cursor.close()
conn.close()