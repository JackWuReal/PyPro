## 如何合并两个字典
用update 方法
```python
dirt1 ={'username':'admin','password':'123456'}
print(dirt1)

dirt2 ={'email':'2845479857@qq.com','address':'sh'}
print(dirt2)

dirt1.update(dirt2) #将dirt2复制并合并到dirt1中
print(dirt1)
print(dirt2)
```