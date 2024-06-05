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

### 参数化
传递数据并参数化
* 场景: 在fixture中的方法里准备测试数据，在测试方法中参数化，测试方法调用准备数据的方法。
* 将两者结合实现数据驱动:
`@pytest.mark.parametrize("login_r", test_user_data,indirect=True)` indeirect=True 
是把login_r当作函数去执行