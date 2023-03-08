s = input("Enter Values Separated by Spaces: ")
nums = s.split()
n = len(nums)

distinct_count = 0

if n > 0:
    distinct_count = 1

    for i in range(1, n):
        if nums[i] != nums[i-1]:
            distinct_count += 1

print("Number of Distinct Elements: ", distinct_count)