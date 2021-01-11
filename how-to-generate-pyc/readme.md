### python程序中间码在什么时候生成，由谁生成？

#### 自动生成

###### 方式1 
```
# 文件1 - script.py
def main():
  print('变量__name__的值是 ' + __name__)

if __name__ == '__main__':
  main()
```

```
# 文件2 - importingScript.py
import script as s

s.main()

# 执行
python3 importingScript.py # 此时会生成pyc文件
python3 script.py # 则不会生成pyc文件
```

在python程序运行过程中，对于import引入的程序会生成pyc文件，对于主程序生成的pyc文件则会在运行结束后删除。

###### 方式2

```
python3 # 进入python解释器

import xxx.py # 在python解释器中执行这个语句后生成pyc文件
```

#### 手动生成
```
# 方法1
python3 -m py_compile xxx.py
python3 -m compileall .

# 方法2
python3 # 进入python解释器

import py_compile
py_compile.compile('xxx.py')
```
所以pyc文件是由python的内置模块py_compile生成。

### 如何执行python程序中间码？

```
python xxx.pyc
```

###### python程序在运行过程中发生了什么？

1.python解释器将源码编译为字节码pyc
2.接着python解释器开始运行pyc字节码
  - pyc字节码编译成机器码
  - 操作系统直接执行机器码

