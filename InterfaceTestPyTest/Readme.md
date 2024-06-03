# Pytest python的单元测试框架
setup_module()
teardown_module()

setup_function()
teardown_function()

setup_class()
teardown_class()

setup_method()
teardown_method()


## 以命令行形式执行  pycharm可配置pytest以命令行方式执行
```shell
Pytest -v (最高级别信息--verbose)
Pytest -v -s filename (输出打印)
Pytest -q (静默)
```
原则
1. pytest将在当前目录及其子马路中运行``test`_*.py``或`*_test.py` 形式的所有文件
2. 以`test_`开头的函数,以`Test`开头的类,以`test_`开头的方法。所有包package都要有`__init__.py`文件
3. Pytest可以执行unittest框架写的用例和方法


## Pytest断言 跳过及运行

```python
import pytest


@(pytest.markif)
```


### 使用自定义标签 eg:@pytest.mark.webtest
# 使用自定义标记只执行部分用例
# @pytest.mark.webtest  @pytest.mark.ios @pytest.mark.android
```shell
pytest -vs test_mark_case.py -m=webtest;
pytest -vs test_mark_case.py -m=ios;
pytest -vs test_mark_case.py -m=android;

```
### @pytest.fixture

### fixture自动应用
不想原测试方法有任何改动,或全部都自动实现自动应用,没特例,也都不需要返回值可以选择自动应用
1. fixture中参数 `autouse=True` 在方法上加`@pytest.fixture(autouse=True)`
2. 使用`@pytest.mark.usefixtures` 在测试方法上加@pytest.mark.usefixtures()

### conftest.py 共享数据
1. 放在项目下为全局共享
2. 放在包下为包共享
3. 文件名字不能改变

### yield与final的故事