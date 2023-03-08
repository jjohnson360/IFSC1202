s = input("Enter Values Separated by Spaces: ")

nums = []
for num_str in s.split():
    nums.append(int(num_str))

for i in range(len(nums)):
    if i % 2 == 1:
        print(nums[i])