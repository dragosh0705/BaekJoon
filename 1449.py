n, l = map(int, input().split())

nums = [int(x) for x in input().split()]

one = 0
far = 0
for i in range(len(nums)):
    #print(abs(nums[i]-nums[i+1]))
    if i+1 < len(nums) and i-1 >= 1:
        if abs(nums[i]-nums[i+1]) == 1:
            one += 1
        elif abs(nums[i]-nums[i+1]) > 1:
            far += 2
       # if abs(nums[i]-nums[i+1]) > 1 and abs(nums[i-1]-nums[i]) > 1:
        #    far += 1
  #  if len(nums) == one+1:
   #     one+=1

finmeter = one + far
count = finmeter / l
rest = finmeter % l
print(one)

if count > 1 and rest != 0: print(int(count)+1)
elif count <= 1: print(int(count))
elif count > 1 and rest == 0: print(int(count))