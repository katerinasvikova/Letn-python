#nums = list(map(int, input().split()))

nums = [0, 1, 4, -4, 8, 1]
#[5, -2, -2, 10, 8]
#[20, -7, -7, -2, 0, 1, 3, 5, 5, 10]
#[0, 1, 4, -4, 8, 1]

#select prime numbers
num_prime = []
def is_prime(num):
    if num in (0,1,-1):
        return False
    for i in range(2, int(abs(num)**0.5)+1):
        if num%i ==0:
            return False
    return True

for num in nums:
    if is_prime(num):
        num_prime.append("TRUE")
    else:
        num_prime.append("FALSE")

print(num_prime)

#find longest sequence of prime numbers
def odd_sequence(nums):
    a=[]
    b=[]
    for idx in range(0, len(nums)):
        if num_prime[idx]=="TRUE" and sum(a) == 0:
            a.append(nums[idx])
        elif num_prime[idx]=="TRUE" and nums[idx] >= nums[idx-1]:
            a.append(nums[idx])
        elif num_prime[idx]=="TRUE" and nums[idx] <= nums[idx-1]:
            a = []
            a.append(nums[idx])
        if num_prime[idx] == "FALSE":
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






