flist = []

for i in range(3):
  def makefunc(i):
    def func(x):
      return x * i
    return func
  flist.append(makefunc(i))

for f in                  :
  print(f(2))
