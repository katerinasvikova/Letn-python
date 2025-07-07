k = int(input())
a = int(input())

sum=0
if a>= 0:
    for i in range(1,a+1,1):
     sum += i**k
else:
   for i in range(a,0,1):
      sum += i**k
print(sum)
