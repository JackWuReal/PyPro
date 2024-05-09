# Linux 命令面试题
* head 和 tail的区别：head是前多少行 tail是后多少行
* sh a >file 2>&1  (重定向)  **标准错误重定向等同于标准输出**,<u>无论是标准输出和标准错误输出,全部都重定向到了file文件中</u>
  * 0 表示标准输入 stdin
  * 1 表示标准输出stdout
  * 2 表示标准错误stderr