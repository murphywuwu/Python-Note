flist = []

for i in range(3):
  def func(x):
    return x*i
  flist.append(func)

for f in flist:
  print(f(2)) 
  # 4，4，4