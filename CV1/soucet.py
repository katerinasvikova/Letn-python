### Uloha 5
a=int(input())
k=3

sum=0
for i in range(1,a+1,1): #(start, cíl, krok)
    sum+=i**k
vzorec = int(((a*(a+1))/2)**2)

print(sum)
print(vzorec)

### Uloha 6
if sum == vzorec:
    print("ANO")
else:
    print("NE")