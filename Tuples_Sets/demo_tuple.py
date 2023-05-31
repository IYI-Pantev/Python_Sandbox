# tuple is read only collection
nums = (1, 2, 4, 4, 4, 6, 7, 8, 9)

print(type(nums))
print(nums[2])
nums = list(nums)
nums.append(33)
print(nums)
nums = tuple(nums)
print(nums)
print(f"num 4 count: {nums.count(4)}")

# return the first index el that encounter
print(f"index of element 8: {nums.index(8)}")