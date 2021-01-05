python程序中间码在什么时候生成，由谁生成？

问题1：在python程序运行过程中，对于import引入的程序会生成pyc文件，对于主程序生成的pyc文件则会在运行结束后删除。

问题2：通过py_compile模块生成。

```
# 方法1
python3 -m py_compile xxx.py
python3 -m compileall .

# 方法2
python3 # 进入python解释器

import py_compile
py_compile.compile('xxx.py')


# 方法3
python3 # 进入python解释器

import xxx.py # 在python解释器中执行这个语句后生成pyc文件
```

如何执行python程序中间码？

```
python xxx.pyc
```

python程序在运行过程中发生了什么？

1.通过python解释器将源码编译为字节码pyc
2.通过python解释器运行pyc字节码
  - pyc字节码编译成机器码
  - 操作系统直接执行机器码

