def outerFunc():
  x = 0
  # x = [1]
  def innerFunc():
    x = 1
    # x.append(2)
    print('inner x:', x)
  
  print('outer x before call inner:', x) # 0
  innerFunc() # 1
  print('outer x after call inner:', x) # 0

# 内部函数无法修改外部函数变量
outerFunc()
