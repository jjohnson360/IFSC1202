s = input("Enter Values Separated by Spaces: ")

nums = []
for num_str in s.split():
    nums.append(int(num_str))

sign = None
for i in range(len(nums) - 1):
    if sign is None:
        sign = nums[i] >= 0
    if (nums[i] >= 0) == sign and (nums[i+1] >= 0) == sign:
        print(nums[i], nums[i+1])
        break
else:
    print()