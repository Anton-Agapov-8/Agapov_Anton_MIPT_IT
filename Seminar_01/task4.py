f = open('input.txt', 'r')
data = list(f.readlines())
nums = list(map(int, data[0].split()))
sign = data[1]
res = nums[0]
for i in range(1, len(nums)):
    if '+' in sign:
        res += nums[i]
    elif '*' in sign:
        res *= nums[i]
    elif '-' in sign:
        res -= nums[i]
f.close()
with open('output.txt', 'w') as f2:
    f2.write(str(res))
