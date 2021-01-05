#!/usr/local/bin/python3
# -*- coding: utf-8 -*- 

def fib(n):
  a, b = 0, 1
  while a < n:
    print(a)
    a, b = b, a+b

def fib2(n):
  result = []
  a, b = 0, 1
  while a < n:
    result.append(a)
    a, b = b, a+b
  return result

# 以脚本的方式执行模块
# python fibo.py <arguments?
# 模块的代码会被执行，就像你导入了模块一样，但是__name__被赋值为__main__
if __name__ == '__main__':
  import sys
  fib(int(sys.argv[1]))