# SQL 查询练习
## 总结
1. 条件查询 where 条件
2. 排序 order by 字段名
3. 聚合函数 count、max、min、sum、avg
4. 分组 group by、分页limit
5. 连接查询 inner join、left join、right join
6. 自关联 inner join
7. 子查询(充当条件或数据源)

数据准备
```sql
DROP table if EXISTS departments;
CREATE TABLE departments(
deptid INT(10) PRIMARY KEY,
deptname VARCHAR(20) NOT NULL
);
insert into departments VALUES('1001','市场部'),('1002','测试部'),('1003','开发部');

SELECT * FROM departments;

drop table if exists employees;
create table employees (
empid int(10) primary key,
empname varchar(20) not null, -- 姓名
sex varchar(4) default null, -- 性别
deptid int(20) default null, -- 部门编号
jobs varchar(20) default null, -- 岗位
politicalstatus varchar(20) default null, -- 政治面貌
leader int(10) default null
);
insert into employees values ('1', '王昭君', '女', '1003', '开发', '群众', '9');
insert into employees values ('2', '诸葛亮', '男', '1003', '开发经理', '群众', null);
insert into employees values ('3', '张飞', '男', '1002', '测试', '团员', '4');
insert into employees values ('4', '白起', '男', '1002', '测试经理', '党员', null);
insert into employees values ('5', '大乔', '女', '1002', '测试', '党员', '4');
insert into employees values ('6', '孙尚香', '女', '1001', '市场', '党员', '12');
insert into employees values ('7', '百里玄策', '男', '1001', '市场', '团员', '12');
insert into employees values ('8', '小乔', '女', '1002', '测试', '群众', '4');
insert into employees values ('9', '百里守约', '男', '1003', '开发', '党员', '9');
insert into employees values ('10', '妲己', '女', '1003', '开发', '团员', '9');
insert into employees values ('11', '李白', '男', '1002', '测试', '团员', '4');
insert into employees values ('12', '孙膑', '男', '1001', '市场经理', '党员', null);

SHOW TABLES;

SELECT * from employees;

drop table if exists salary;
create table salary (
sid int(10) primary key,
empid int(10) not null,
salary int(10) not null -- 工资
);

insert into salary values ('1', '7', '2100');
insert into salary values ('2', '6', '2000');
insert into salary values ('3', '12', '5000');
insert into salary values ('4', '9', '1999');
insert into salary values ('5', '10', '1900');
insert into salary values ('6', '1', '3000');
insert into salary values ('7', '2', '5500');
insert into salary values ('8', '5', '2000');
insert into salary values ('9', '3', '1500');
insert into salary values ('10', '8', '4000');
insert into salary values ('11', '11', '2600');
insert into salary values ('12', '4', '5300');
```
```sql
-- 1、列出总人数大于4的部门号和总人数。

show TABLES;
DESC employees;
desc departments;

SELECT deptid,COUNT(*) FROM employees GROUP BY deptid HAVING COUNT(*) >= 0;
SELECT COUNT(*) FROM employees;
SELECT * FROM employees;


-- 2、列出开发部和和测试部的职工号、姓名。

SELECT empid,empname,deptname FROM employees emp INNER JOIN departments dep on emp.deptid = dep.deptid WHERE dep.deptname IN('开发部','测试部');

-- 3、求出各部门党员的人数，要求显示部门名称。

SELECT dep.deptname,emp.deptid,COUNT(*) from employees emp INNER JOIN departments dep on emp.deptid=dep.deptid GROUP BY deptid,politicalstatus HAVING politicalstatus='党员';

SELECT emp.deptid,deptname,COUNT(*) from employees emp INNER JOIN departments dep on emp.deptid=dep.deptid WHERE politicalstatus='党员' GROUP BY deptid;


SELECT deptid,politicalstatus,COUNT(*) FROM employees GROUP BY deptid,politicalstatus HAVING ;

-- 4、列出市场部的所有女职工的姓名和政治面貌。
-- 5、显示所有职工的姓名、部门名和工资数。
-- 6、显示各部门名和该部门的职工平均工资。
-- 7、显示工资最高的前3名职工的职工号和姓名。
-- 8、列出工资在1000－2000之间的所有职工姓名。
-- 9、列出工资比王昭君高的员工。
-- 10、列出每个部门中工资小于本部门平均工资的员工信息。 
```
