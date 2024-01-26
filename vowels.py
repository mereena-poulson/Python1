n=input("enter the word")
print("the string are",n)
print("the vowels are",end="")
for i in n:
  if i in 'aeiouAEIOU':
    print([i],end="")