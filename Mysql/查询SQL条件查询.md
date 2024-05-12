## 条件查询
* 条件查询：比较运算符
    * 大于> 等于= 小于< 大于等于>= 小于等于 不等于(<>或者!=)
```sql
select age from students WHERE name = '小乔';

select * from students WHERE age < 20;

select * from students where hometown != '北京';

select card from students WHERE studentNo='007';

SELECT * from students WHERE class!='1班';

SELECT * from students WHERE class<>'2班';

select name,sex,age from students WHERE age>=20;

desc students;
```
* 条件查询：逻辑运算符 
  * and 且 、or 符合其一 、not 非 不符合
```sql
select * from students WHERE age =19 and sex='女';

SELECT * from students WHERE sex = '女' or class = '1班';

select * from students WHERE hometown !='天津';
-- where NOT 条件
SELECT * from students where not hometown='天津';

select * FROM students where hometown='河南' or hometown='河北';

select * from students;

SELECT * from students WHERE class='2班' AND hometown='上海';

SELECT * from students WHERE not age=20;
```
* 条件查询：模糊查询
  * like 关键字
    * % 匹配任意个字符
    * _ 匹配任意单个字符
    * 一般like关键字只用来匹配字段类型为字符串的
```mysql
SELECT * FROM students WHERE name LIKE'孙_';
SELECT * FROM students WHERE name LIKE'孙%';

SELECT * from students WHERE name LIKE'%乔';

SELECT * FROM students WHERE `name` LIKE'%白%';

SELECT * FROM students WHERE `name` LIKE'__';

SELECT * from students WHERE `name` LIKE'百%' and age>20;

SELECT * FROM students WHERE studentNo LIKE'%1';
```
* 条件查询: 范围查询
  * in: 查询非连续范围内的数据
`SELECT * from students WHERE hometown IN ('北京','上海','广东');`
  * between and 查询连续范围内的数据
`SELECT * FROM students WHERE age BETWEEN 18 AND 23;`
```sql
SELECT * FROM students WHERE age IN (18,19,22) AND sex='女';

SELECT * from students WHERE NOT age BETWEEN 20 AND 25;
```

* 条件查询：为空判断
  * Null 和空字符串不一样
  * 空判断: is null
  * 非空判断: is not null
```sql
SELECT * from students WHERE card is null;

SELECT * from students WHERE card is NOT null; 
```
### 排序
* 字段的排序规则默认升序排列
* asc:升序,从小到大排列
* desc:降序,从大到小排列
```mysql
SELECT * from students ORDER BY age DESC;

SELECT * from students ORDER BY age DESC,studentNo;

-- 查询所有学生信息，按班级从小到大排序，班级相同时再按学号从小到大排序
SELECT * FROM students ORDER BY class,studentNo ASC; 
```
***
## 分组&&聚合
### 聚合函数
* 使用聚合函数方便进行数据统计
* 聚合函数不能在where中使用
  * count()
    * count(*)表的总记录数
  * max()
  * min()
  * sum()
  * avg()
```mysql

SELECT name FROM students;
SELECT card FROM students;

SELECT count(age) FROM students;
SELECT count(*) FROM students;

SELECT MAX(card) FROM students;
SELECT MAX(studentNo) FROM students;

SELECT avg(age) FROM students WHERE sex='女';
SELECT MAX(age) FROM students WHERE sex='女';
SELECT min(age) FROM students WHERE not sex='男';

SELECT class,age,name FROM students WHERE class='1班';
SELECT min(age) FROM students WHERE class='1班';

SELECT age FROM students WHERE hometown='北京';
SELECT SUM(age) FROM students WHERE hometown='北京';

SELECT MAX(age),MIN(age),AVG(age),SUM(age) FROM students;

SELECT COUNT(*) FROM students WHERE class in('1班','2班');
SELECT COUNT(*) FROM students WHERE class='1班' OR class='2班';
SELECT * FROM students WHERE class BETWEEN '1班' and '2班';

SELECT COUNT(*) FROM students WHERE class IN('1班','2班');
SELECT COUNT(*) FROM students WHERE class = '1班';

SELECT COUNT(*) FROM students WHERE class='3班' and age<18;
```
### 分组查询
* 分组查询的目的是对每一组数据进行统计(使用聚合函数)
  * select 字段名1,字段名2,聚合函数 from 表名 group by 字段名1,字段名2;
```mysql
SELECT sex,count(*) from students GROUP BY sex;
SELECT age,COUNT(*) FROM students GROUP BY age;
SELECT sex,MAX(age) FROM students GROUP BY sex;
SELECT sex,min(age) FROM students GROUP BY sex;
-- 查询每个班级的人数
SELECT class,COUNT(*) FROM students GROUP BY class;
-- 查询每个班级每种性别人数
SELECT class,sex,COUNT(*) FROM students GROUP BY class,sex; 
```
#### 分组之后数据筛选
* 将分组之后的数据当成一个表数据,然后再通过having条件 来对当前表数据进行筛选
* 语法``select 字段名1,字段名2,聚合函数 from 表名 group by 字段名1,字段名2 having 条件`
  * having也是条件运算符类似 where
  * having后面可以有聚合函数

**where 和 having的区别**

* where 是对from 后面的表进行数据筛选,属于对原始数据的筛选
* having是对group by的结果进行筛选
* having后面可以是聚合函数where后面不可以
***
## 分页查询
* 语法格式：`sleect * from 表名 limit start,count`
  * start 表示开始的记录,索引是由0开始.0表示第一条记录
    * 从第0条开始可以省略不写、该`SELECT * FROM students LIMIT 8;`语句表示查询默认前八条数据
  * count表示的是从start开始,查询多少条记录
  * 分页查询实现
    * `select * from 表名 limit (总页数-1)*每页记录数,每页记录数`;
    * eg：为查询第四页数据,每页为3条数据`SELECT * FROM students LIMIT 9,3;`
```mysql
SELECT * FROM students LIMIT 6,10;
-- 默认前三条数据
SELECT * FROM students LIMIT 3;
-- 默认前八条数据
SELECT * FROM students LIMIT 8;

SELECT * from students LIMIT 9,3;
SELECT * from students LIMIT 10,5;

SELECT * from students LIMIT 1,5;
SELECT * FROM students LIMIT 9,3;
```
