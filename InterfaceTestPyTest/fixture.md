## fixture
1. fixture详解：
fixture概念：fixture是pytest用于将测试前后进行预备、清理工作的代码处理机制

2. fixture对于setup teardown有以下优势
* 更加灵活、小巧、方便
* `conftest.py` 配置里面可以实现全局数据共享

3. 作用域


* name
* scope
* autouse
* params:
  * 
  * 这里有一个request参数 用于接收fixture的返回结果,并通过request.param返回结果内容
* ids