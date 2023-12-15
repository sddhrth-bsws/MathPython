"""
target = 5
sol = []
size = len(nums)
for i in range(0,size):
    for j in range((i+1),size):
        if(nums[i]+nums[j] == target):
            sol.append(i)
            sol.append(j)
print(sol)
"""
x = 5
y = 2
print(x/y) #exact value
print(x//y) # integer quotient