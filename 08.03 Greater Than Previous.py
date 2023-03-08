s = input("Enter Values Separated by Spaces: ")

nums = []
for num_str in s.split():
    nums.append(int(num_str))

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        print(nums[i])