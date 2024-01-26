a=[1,2.4,5,7,8]
b=[3,5,7,8,9,2]
s=int(0)
c=int(0)
if len(a)==len(b):
 print("List of same length")
else:
 print("lists have different length")
 for i in range(0,len(a),len(b)):
   s=s+a[i]
    c=c+b[i]
    if(s==c):
      print("equal sum")
else:
  print("not smae sum")
  print("elements that matched are:")
  l=[]
  for i in range(0,len(a)):
    for j in range(0,len(b)):
      if a[i]==b[i]:
        i.append(a[i] and b[i])
  else:
    continue
    print(i)