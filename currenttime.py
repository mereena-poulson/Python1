class time:
  def __init__(self,hour,minute,second):
    self.hour=hour
    self.minute=minute
    self.second=second
  def __add__(self,tm):
    print("hour",self.hour+tm.hour)
    print("minute",self.minute+tm.minute)
    print("second",self.second+tm.second)

h1=int(input("enter hour"))
m1=int(input("enter minute"))
s1=int(input("enter second"))
obj=time(h1,m1,s1)
h2=int(input("enter hour"))
m2=int(input("enter minute"))
s2=int(input("enter second"))
obj2=time(h2,m2,s2)
obj+obj2