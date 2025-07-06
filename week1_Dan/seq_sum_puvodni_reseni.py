nums = list(map(int, input().split()))


def isPrime(num):
    prime = abs(num)
    if prime > 1:
        for i in range(2, prime):
            if (prime % i) == 0:
                return False
        else:
            return True


max_len = 0
cnt = 0
for i in range(len(nums)):
    cnt_now = 0
    now_len = 0
    if (isPrime(nums[i]) == True):
        now_len = 1
        cnt_now = i
        while i + 1 < len(nums) and (nums[i] <= nums[i + 1]) and (isPrime(nums[i + 1]) == True):
            now_len += 1
            i += 1
    if max_len <= now_len:
        if max_len < now_len:
            max_len = now_len
            cnt = cnt_now
        if max_len == now_len:
            mlcnt = 0
            nlcnt = 0
            for i in range(max_len):
                mlcnt += nums[cnt + i]
            for i in range(now_len):
                nlcnt += nums[cnt_now + i]
            if mlcnt < nlcnt:
                max_len = now_len
                cnt = cnt_now

print(max_len)
sum_cnt = 0
for i in range(max_len):
    sum_cnt += nums[cnt + i]
print(sum_cnt)