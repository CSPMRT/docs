***************
fipy 安装方法
***************

.. note:: 
   作者：Chen Longhao   时间：2020年6月25日

简介
-----
fipy 是一个基于Python的使用有限体积法的偏微分方程数值求解器，由美国国家标准与技术研究院开发，
fipy官网为： https://www.ctcms.nist.gov/fipy/

安装方法
---------

1.安装python3-gmsh和python3-petsc4py

.. code-block::

   sudo apt install python3-gmsh python3-petsc4py

2.安装mpi4py及fipy

.. code-block:: 

   pip3 install mpi4py
   pip3 install fipy

至此，fipy及其所需环境应该已经安装完成

测试方法
---------

串行运行测试：

.. code-block:: 

   python3 -c "import fipy; fipy.test('--petsc')"

并行运行测试：

.. code-block:: 

   mpirun -np 你的处理器个数 python3 -c "import fipy; fipy.test('--petsc')"
