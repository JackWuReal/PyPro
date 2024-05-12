# 基础sql语句
## 建表 CREATE
```sql
-- CREATE 建表语句
create table students(
studentNo VARCHAR(10) primary key,
name VARCHAR(10),
sex VARCHAR(1),
hometown VARCHAR(20),
age tinyint(4),
class VARCHAR(10),
card varchar(20)
);

insert into students values
('001', '王昭君', '女', '北京', '20', '1班', '340322199001247654'),
('002', '诸葛亮', '男', '上海', '18', '2班', '340322199002242354'),
('003', '张飞', '男', '南京', '24', '3班', '340322199003247654'),
('004', '白起', '男', '安徽', '22', '4班', '340322199005247654'),
('005', '大乔', '女', '天津', '19', '3班', '340322199004247654'),
('006', '孙尚香', '女', '河北', '18', '1班', '340322199006247654'),
('007', '百里玄策', '男', '山西', '20', '2班', '340322199007247654'),
('008', '小乔', '女', '河南', '15', '3班', null),
('009', '百里守约', '男', '湖南', '21', '1班', ''),
('010', '妲己', '女', '广东', '26', '2班', '340322199607247654'),
('011', '李白', '男', '北京', '30', '4班', '340322199005267754'),
('012', '孙膑', '男', '新疆', '26', '3班', '340322199000297655');
```
## 查询语句 SELECT语句
```sql
-- 查询部分字段
select name,sex,age from students;

-- 取别名 为关联查询做准备
select s.name,s.sex,s.age from students as s;

-- 去重 根据性别去重
SELECT DISTINCT sex from students;

SELECT DISTINCT age from students;

SELECT age from students;
```
## 添数据 Insert语句
```sql
-- 逐一添加
-- insert into students (id,name) values(0,'张三');
-- insert into students (id,name) values(0,'李四');
insert into students values(0,'李四',20,180);

-- 全字段填写
insert INTO students VALUES(0,'mike',18,1.66);

-- 部分字段填写
insert into students(name) values ('tom');

-- 一行插入多条数据,全部字段
insert into students VALUES(0,'lily',19,1.68),(0,'yoyo',20,1.98),(0,'mark',20,8866);

-- 一行插入多条数据,部分字段
insert into students(name,height) VALUES('falfjdajfdjafdjalfjdjafjdlajflddjkla',2222.222),('mmmm',3333.333);

-- 方法二通过一条语句insert插入多条数据,数据之间用逗号隔开
-- insert into 表名 values(),()...
insert into students values(0,'亚瑟王',23,167.89),(0,'亚瑟四',25,178.23);

-- insert into 表名 (字段名1,字段名2,字段名3...) VALUES(字段1,字段2,字段3...),(字段1,字段2,字段3...)
insert into students (id,name) values(0,'小黑'),(0,'小蓝'),(NULL,'大白');
```
## 更新数据语句 update 语句
```sql
-- UPDATE 表名 set 字段名1=值1,字段名2=值2...... WHERE 条件
-- 修改id为5的数据，将名称设置为狄仁杰 年龄设为22
update students set name='狄仁杰',age=22 WHERE id=5;
```
## 删除语句 DELETE TRUNCATE DROP 语句
三种删除数据的方式区别
1. delete：可以通过where子句删除部分记录
   * 删除所有数据时,自增长字段不会从1开始
2. truncate：Truncate删除数据时表结构会保留,自增长字段从1开始.执行效率低于drop
3. drop: 删除表,效率高
```SQL
-- delete from 表名 where 条件(物理删除)

DELETE from students where age >= 25;

DELETE FROM students where id = 5;

-- 逻辑删除是指通过设定一个字段来标识当前记录已经删除
-- is_delete字段来标识，1代表删除，0代表未删除

-- 清楚表中所有数据,但表结构会保留,自增长字段的值会从1开始
TRUNCATE table students;

-- drop table 表名(删除数据表，包括数据和表结构)
drop table students;

drop table if exists students;
```

