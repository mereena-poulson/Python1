class rect:
     def __init__(self, l,b):
        self.length = l
        self.breadth = b
     def  area(self):
        self.area=self.length*self.breadth
        print("area=",self.area)
     def __lt__(self,second):
        if self.area < second.area:
          return True
        else:
          return False
print("first rectangle")
len1=int(input("enter the length:"))
bread1=int(input("enter the breadth:"))
obj1=rect(len1,bread1)
obj1.area()
print("second rectangle")
len2=int(input("enter the length:"))
bread2=int(input("enter the breadth:"))
obj2=rect(len2,bread2)
obj2.area()
if obj1< obj2:
  print("second is larger")
else:
  print("first is larger")