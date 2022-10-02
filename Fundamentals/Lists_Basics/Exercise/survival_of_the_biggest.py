# Write a program that receives a list of integer numbers
# and a number n. The number n represents the amount of
# numbers to remove from the list. You should remove the smallest ones.

data = input().split()

n = int(input())


nums = [int(x) for x in data]

nums.sort()
print(f"Numbers list before smallest cut {nums}.")
print(nums[n:])