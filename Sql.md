# Mysql数据库面试题
1. SQL的分类
    * DQL:数据查询语句 select
    * DML：数据操作语句 insert、update、delete
    * TPL：事务处理语句 begin、transaction、 commit、rollback
    * DCL：数据控制语句 grant、revoke
    * DDL：数据定义语句 create 、 drop
    * CCL：指针控制语句 declare、cursor
2. drop、delete、truncate 三者的区别
2. 什么是事务?
    事务：是数据库操作的最小工作单元，是作为单个逻辑工作单元执行的一系列操作；这些操
作作为一个整体一起向系统提交，要么都执行、要么都不执行；事务是一组不可再分割的操
作集合（工作逻辑单元）；
    1. 原子性(Atomicity)：事务中的全部操作在数据库中是不可分割的，要么全部完成，要
    么均不执行。
    2. 一致性(Consistency)：几个并行执行的事务，其执行结果必须与按某一顺序串行执行
    的结果相一致。
    3. 隔离性(Isolation)：事务的执行不受其他事务的干扰，事务执行的中间结果对其他事
    务必须是透明的。
    4. 持久性(Durability)：对于任意已提交事务，系统必须保证该事务对数据库的改变不
    被丢失
3. SQL中的聚合函数都有哪些?
   * max():最大
   * min()：最小
   * avg()：平均
   * sum()：求和
   * count()：统计总数
4. 主键、外键、索引的区别
   1. 定义
      * 主键：唯一标识一条记录，**不能有重复的，不允许为空**
      * 外键：表的外键是另一表的主键, **外键可以有重复的**, 可以**是空值**
      * 索引：该字段没有重复值，但可以有一个空值
   2. 作用
      * 主键：用来保证**数据完整**性
      * 外键：用来和其他表**建立联系**用的
      * 索引：提高**查询排序**的速度
   3. 个数
      * 主键：只能有一个
      * 外键：一个表可以有多个外键
      * 索引：一个表可以有多个索引

7. InnoDB索引和MyISM索引的区别，索引的优缺点
参考答案:
1）存储结构（主索引／辅助索引）
InnoDB 的数据文件本身就是主索引文件。而 MyISAM 的主索引和数据是分开的。
InnoDB 的辅助索引 data 域存储相应记录主键的值而不是地址。
而 MyISAM 的辅助索引和主索引没有多大区别。
innoDB 是聚簇索引，数据挂在逐渐索引之下。
2）锁: MyISAM 使用的是表锁；InnoDB 使用行锁
3）事务: MyISAM 没有事务支持和 MVCC；InnoDB 支持事务和 MVCC
4）全文索引: MyISAM 支持 FULLTEXT 类型的全文索引;InnoDB 不支持 FULLTEXT 类型的全
文索引，但是 InnoDB 可以使用 sphinx 插件支持全文索引，并且效果更好
5）主键: MyISAM 允许没有任何索引和主键的表存在，索引都是保存行的地址; InnoDB
如果没有设定主键或非空唯一索引，就会自动生成一个 6 字节的主键，数据是主索引的一部
分，附加索引保存的是主索引的值
6）外键: MyISAM 不支持；InnoDB 支持
8. 列举几种表连接的方式,有什么区别
   * 左连接：左边为主表表数据全部显示, 匹配表的不匹配部分不显示
   * 右连接：右边为主表表数据全部显示, 匹配表的不匹配部分不显示
   * 内连接：只有两个元素表相匹配的才能在结果集中显示
   * 全外连接：连接中的不匹配的数据全部会显示出来
   * 交叉连接：笛卡尔乘积, 显示的结果是连接表数的乘积
9. 乐观锁和悲观锁的区别
10. 工作中哪些方面使用到了数据库?如何使用？
11. 
    1. 用SQL语句查询出每门课都大于80分的学生姓名。表scores如下：
   ```mysql
   select name,min(score) from scores group by name having min(score)>80;
   ```
   2. 用sql语句查询两门以上不及格课程的同学的学号以及其平均成绩，并按成绩排序表结构如下：
   ```mysql
   select student.id, student.stdentname,AVG(student_score.score) from student,student_score where
   student_id = student_score.id and student_score.score<60 group by student_score.id having count(*)>1;                                                                                            
   ```