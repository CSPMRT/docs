**************************************
Hello World运行背后（一）——编译
**************************************

.. metadata::
    Chen Longhao
    2020,08,07

此文是 ``Hello World运行背后`` 系列文章的第一篇，主要内容是一个程序（C++）编译的详细过程。

首先，我们来看一个非常简单的程序

.. literalinclude:: code/HelloWorld.cpp
    :language: cpp
    :linenos:

如果要编译运行这个程序，我们通常会这样做::

    g++ -o HelloWorld HelloWorld.cpp    #编译
    ./HelloWorld    #运行

编译看似好像是一步完成的，实则经历了以下4个过程：

.. image:: images/CompilationProcess.png

现在我们一步一步来执行上述过程，看看每一步究竟经历了什么。

1.预处理
------------
预处理可以使用命令 ::

    g++ -E HelloWorld.cpp -o HelloWorld.i

来完成，预处理之后得到的文件是 ``HelloWorld.i``，因为内容很多，所以我将其作为一个单独的文档输出，见： :doc:`code/HelloWorld_i`

可以看到，其实预处理就是把头文件包含进来、展开宏、除去注释。

2.编译
--------
这里的编译是指将预处理后的文件编译成汇编代码的过程，具体可以使用命令 ::

    g++ -S HelloWorld.i -o HelloWorld.s

编译后生成的汇编文件如下

.. literalinclude:: code/HelloWorld.s
    :language: asm
    :linenos:

3.汇编
--------
汇编就是将编译出的代码转换为机器代码，具体可以用命令 ::

    g++ -c HelloWorld.s -o HelloWorld.o

这一步生成的是二进制文件，用 ``file`` 可以看到文件类型 ::

    $ file HelloWorld.o
    HelloWorld.o: ELF 64-bit LSB relocatable, x86-64, version 1 (SYSV), not stripped

我们可以用 ``objdump HelloWorld.o -h -x -d -s`` 来查看文件内容并对其反汇编，结果如下：

.. literalinclude:: code/HelloWorld_o_objdump
    :linenos:

4.链接
---------
链接就是将汇编后的文件与所需的库文件链接成最终的可执行文件，具体可以使用命令 ::

    g++ HelloWorld.o -o HelloWorld

来实现，现在得到的文件就是可执行文件，我们可以直接执行 ::

    $ ./HelloWorld
    Hello World

我们可以用 ``file`` 查看文件类型 ::

    $ file HelloWorld
    HelloWorld: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=9f16c87165c6f27278c4123fa00647a78c40c1ce, not stripped

我们可以看到，这个可执行文件是使用的 ``/lib64/ld-linux-x86-64.so.2`` 这一个动态链接库，
当然，我们也可以用 ``objdump HelloWorld -h -x -d -s`` 来查看文件内容并对其反汇编，结果有点长，见 :doc:`code/HelloWorld_objdump`

结束
-------
以上就是一个程序编译成可执行文件的过程，当然，在实际的使用过程中，编译器往往可以自动完成这一些。

下一篇文章，我们打算探讨执行 ``./HelloWorld`` 后发生了什么。