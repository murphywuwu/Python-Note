# encoding: utf-8

import sys
import os

# 方式1, 5
# 加入path路径
sys.path.append(os.path.dirname(__file__))
print(sys.path)
import a

# 相对导入
# from . import a

# 绝对导入
# import simple_package.a

# 方式2
# from a import bar

# 相对导入
# from . import bar

# 绝对导入
# from simple_package.a import bar
