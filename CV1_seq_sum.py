#nums = list(map(int, input().split()))

nums = [0, 1, 4, -4, 8, 1]

#select which numbers are odd
num_odd =[]
for num in nums:
    def is_odd(num):
        if num%2 == 1:
            num_odd.append("TRUE")
        elif num%2 == 0.5:
            num_odd.append("TRUE")
        else: 
            num_odd.append("FALSE")
    is_odd(num)

#find longest sequence of odd numbers
def odd_sequence(nums):
    a=[]
    b=[]
    for idx in range(0, len(nums)):
        if num_odd[idx]=="TRUE":
            a.append(nums[idx])
        elif num_odd[idx] == "FALSE":
            if len(a) > len(b):
                b = a
                a = []
            elif len(a) == len(b):
                if sum(a) > sum(b):
                    b = a
                    a = []
    print(len(b)) #print lenght of sequence
    print(sum(b)) #print the sum of sequence
    print(b) #print the sequence

print(odd_sequence(nums))






