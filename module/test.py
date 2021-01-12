# encoding: utf-8

# 方式1
# import simple_package

# simple_package.a.bar() 
# python:AttributeError: module 'simple_package' has no attribute 'a'
# python3:执行失败

# 方式2
# import simple_package

# simple_package.bar()
# python3:执行失败

# 方式3
# from simple_package.a import bar, foo

# bar()
# foo()

# 方式4
# import simple_package.a

# simple_package.a.bar()

# 方式5
from simple_package import a
a.bar()
# python3 执行失败# ModuleNotFoundError: No module named 'a'
