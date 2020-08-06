***********************
Python 实现排序链表
***********************

.. metadata::
    Chen Longhao
    2020,08,06

.. warning::
   这是一个演示程序，没有经过充分测试，请不要用于生产环境

.. code-block:: python
    
    class link:

        # 节点
        class node:
            def __init__(self, data):
                self.prev = None
                self.next = None
                self.data = data

        def __init__(self):
            self.HEAD = None

        # 添加数据
        def add(self, data):
            if self.HEAD == None:
                self.HEAD = self.node(data)
            else:
                p = self.HEAD
                new_node = self.node(data)
                if data <= p.data:
                    new_node.next = p
                    self.HEAD = new_node
                    return

                while p.next != None and data > p.next.data:
                    p = p.next

                new_node.next = p.next
                p.next = new_node

        # 读取数据，以列表形式返回
        def read(self):
            p = self.HEAD
            res = []
            while p != None:
                res.append(p.data)
                p = p.next
            return res


    """
    以下为测试代码
    """
    import random
    import time

    a = link()
    num = 20000  # 要测试的数据量
    s_t = time.time()
    for i in range(num):
        a.add(int(random.random() * 1000))

    c_t = time.time()

    data = a.read()
    e_t = time.time()

    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            print(data)
            print("ERROR")
            exit(-1)
        print(i)
    print("PASS")

    # 打印单个数据添加和读取的平均时间，以毫秒为单位
    print((c_t - s_t) / num * 1000, "   ", (e_t - c_t) / num * 1000)