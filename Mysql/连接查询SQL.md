# 连接查询、自关联、子查询
## 连接查询概述
* 内连接:连接两个表时,取两个表中都存在的数据,取交集
* 左连接:连接两个表时,取左表中特有的数据,对于右表中不存在的数据用null来填充
* 右连接:连接两个表时,取右表中特有的数据,对于左表中不存在的数据用null来填充
![img.png](img.png)

**数据准备**
```sql
CREATE TABLE courses(
courseNo INT(10) UNSIGNED PRIMARY KEY auto_increment,
name VARCHAR(10)
);
SELECT * from courses;

insert into courses VALUES ('1','数据库'),('2','qtp'),('3','linux'),
('4','系统测试'),('5','单元测试'),('6','测试过程');

drop table if exists scores;
show tables;
create table scores (
id int(10) unsigned primary key auto_increment,
courseNo int(10),
studentno varchar(10),
score tinyint(4)
);

insert into scores values ('1', '1', '001', '90'), ('2', '1', '002', '75'),
('3', '2', '002', '98'),('4', '3', '001', '86'),('5', '3', '003', '80'),
('6', '4', '004', '79'),('7', '5', '005', '96'),('8', '6', '006', '80');

SELECT * from scores;
```
### 内连接
* 语法格式: `select * from 表名1 inner join 表名2 on 表1.列=表2.列;`
  * 两表的列一定存在关联关系
  * 内连接连接时可以连接多个表
```sql
SELECT * FROM students INNER JOIN scores on students.studentNo=scores.studentNo;

SELECT * from students as stu INNER JOIN scores as sco on stu.studentNo=sco.studentNo;
-- 别名可以不写as
SELECT * from students stu INNER JOIN scores sco on stu.studentNo=sco.studentNo;

SELECT * from students stu,scores sco WHERE stu.studentNo=sco.studentNo;

-- 查询课程信息与课程成绩
SELECT * FROM courses cou INNER JOIN scores sco on cou.courseNo=sco.courseNo;

SELECT name,stu.studentNo,courseNo,score FROM students stu INNER JOIN scores sco ON stu.studentNo = sco.studentNo WHERE name='王昭君';

-- 查询学生信息及学生课程对应的成绩
SELECT * from students stu INNER JOIN scores sco on stu.studentNo=sco.studentNo INNER JOIN courses cou on sco.courseNo=cou.courseNo;

-- 所有学生的数据库成绩要求显示姓名课程名成绩
SELECT stu.name,cou.name,score from courses cou INNER JOIN scores sco on cou.courseNo=sco.courseNo INNER JOIN students stu on sco.studentNo=stu.studentNo WHERE cou.name='数据库';

SELECT stu.name,cou.name,score from courses cou INNER JOIN scores sco on cou.courseNo=sco.courseNo INNER JOIN students stu on sco.studentNo=stu.studentNo WHERE stu.name='王昭君' and cou.name='数据库';

SELECT stu.name,cou.name,MAX(score) from scores sco INNER JOIN courses cou on sco.courseNO = cou.courseNo INNER JOIN students stu on sco.studentNo=stu.studentNo WHERE stu.sex='男' ;

-- 男生中分数最高的人
SELECT stu.name,cou.name,score from scores sco INNER JOIN courses cou on sco.courseNO = cou.courseNo INNER JOIN students stu on sco.studentNo=stu.studentNo WHERE sex='男' ORDER BY score DESC LIMIT 0,1 ;
```
### 左连接
* 语法格式: `select * from 表1 left join 表2 on 表1.列=表2.列`
* 左连接查询的是左表特有的数据,对于右表中不存在的数据用null来填充
```sql
-- 查询所有学生成绩包括没有成绩的学生
SELECT * from students stu left JOIN scores sco on stu.studentNo=sco.studentNo;

-- 查询所有学生成绩包括没有成绩的学生需要显示课程名

SELECT * from students stu LEFT JOIN scores sco ON stu.studentNo=sco.studentNo LEFT JOIN courses cou ON sco.courseNo= cou.courseNo;
```
### 右连接
* 语法格式:`select * from 表1 right join 表2 on 表1.列=表2.列`
* 右连接查询的是右表特有数据对于左表中不存在的数据用null填充
```sql
-- RIGHT JOIN
SELECT * from scores RIGHT JOIN students ON scores.studentNo = students.studentNo;

-- 查询所有学生成绩包括没有成绩的学生需要显示课程名
select * from scores
right join courses on scores.courseNo = courses.courseNo
right join students on students.studentNo = scores.studentNo
```
***
## 自关联
### 自关联介绍
* 自连接运用场景
  * 省市区信息，一般不会放在不同表里进行存储,而是放在同一个表中。
  * 数据准备
```sql
drop table if exists areas;

create table areas(aid int primary key, atitle varchar(20),pid int);
insert into areas values ('130000', '河北省', NULL), ('130100', '石家庄市','130000'),
('130400','邯郸市','130000'), ('130600', '保定市', '130000'),('130700','张家口市', '130000'),
('130800', '承德市', '130000'),('410000', '河南省', NULL), ('410100', '郑州市', '410000'),
('410300', '洛阳市', '410000'),('410500', '安阳市', '410000'),('410700', '新乡市', '410000'),
('410800', '焦作市', '410000'),('410101', '中原区', '410100'),('410102', '二七区', '410100'),
('410301', '洛龙区', '410300');
```
### 自关联实现
* 通过自关联查询时当前关联的表当中一定会存在两个相关联的字段
* 自关联要用别名
* 语法格式`select * from 表名 as 别名1 inner join 表名 as 别名2 on 别名1.列=别名2.列`
```sql
-- 查询河南省所有的市
SELECT * from areas AS a1 INNER JOIN areas as a2 on a1.aid = a2.pid WHERE a1.atitle='河南省';

SELECT * from areas AS a1 INNER JOIN areas as a2 on a1.aid = a2.pid WHERE a1.atitle='郑州市';
-- 查询河南省所有的市和区
SELECT * from areas AS a1 INNER JOIN areas as a2 on a1.aid = a2.pid left JOIN areas as a3 ON a2.aid=a3.pid WHERE a1.atitle='河南省';

SELECT * from areas AS a1 left JOIN areas as a2 on a1.aid = a2.pid LEFT JOIN areas as a3 ON a2.aid=a3.pid WHERE a1.atitle='河南省';

select * from areas as a1 inner join areas as a2 on a1.aid=a2.pid where a1.atitle='河北省';
-- 查询洛阳市所有的区
select * from areas as a1 inner join areas as a2 on a1.aid=a2.pid where a1.atitle='洛阳市';
```
## 子查询

* 将一条sql查询语句嵌入在其他的SQL语句中,被嵌入的SQL称为子查询,其他SQL称之为主查询
  * 子查询select 语句要么充当条件要么充当数据源
  * 子查询语句是一条完整的select语句且可以单独执行
  * 特定关键词 any in some 同一个意思 / != all 相当于 not in
### 子查询充当条件
```sql
-- 标量子查询
SELECT * from scores WHERE studentNo=(SELECT studentNo FROM students WHERE name='王昭君');

-- 查出18岁学生的成绩，要求显示成绩
-- 列子查询
select * from scores WHERE studentNo IN(select studentNo FROM students WHERE age='18');

-- 查询和王昭君同班同龄的学生信息
-- 行子查询
SELECT class,age FROM students WHERE name='王昭君';

SELECT * from students WHERE (class,age)=(SELECT class,age FROM students WHERE name='王昭君');
```
### 子查询充当数据源
```sql
-- 子查询充当数据源
SELECT * from courses WHERE name in('数据库','系统测试')

SELECT * from scores as sc INNER JOIN(SELECT * from courses WHERE name in('数据库','系统测试')) as co ON sc.courseNo=co.courseNo;

select studentNo from students where age=18;
select score from scores where studentNo in (select studentNo from students where age=18);
-- =any和in等价
select score from scores where studentNo = any(select studentNo from students where age=18);
-- SOME:是ANY的别称,很少用
select score from scores where studentNo = some(select studentNo from students where age=18);

-- != all 和 not in 等价
select score from scores where studentNo not in (select studentNo from students where age=18);
select score from scores where studentNo != all(select studentNo from students where age=18);


-- 1、 查询大于平均年龄的学生
select avg(age) from students;
select * from students where age > (select avg(age) from students);

-- 2、 查询年龄在18-20之间的学生的成绩
select * from students where age between 18 and 20;
select * from scores as sc inner join (
select * from students where age between 18 and 20
) as stu on sc.studentNo=stu.studentNo;

```