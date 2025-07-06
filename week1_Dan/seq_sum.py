nums = list(map(int, input().split()))

def isPrime(num):
    "is the number prime"
    if num <= 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

def check_sequence(a,b):
    if len(b) < len(a):
        b = a.copy()
        a = []
    if len(b) == len(a):
        if sum(b) < sum(a):
            b = a.copy()
            a = []
    return a,b

def find_sequence(nums):
    "find the longest rising sequence of prime numbers from a list "
    a = []
    b = []
    for i in range(len(nums)):
        num = nums[i]
        if len(a) == 0:
            if isPrime(abs(num)):
                a.append(num)
        else:
            if isPrime(abs(num)):
                if a[-1] <= num:
                    a.append(num)
                else:
                    a,b = check_sequence(a,b)
                    a = []
                    a.append(num)
            else:
                a,b = check_sequence(a,b)



    print(len(b)) # prvni radek output
    print(sum(b)) # druhy radek output


find_sequence(nums)