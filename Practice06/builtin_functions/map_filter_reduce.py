from functools import reduce

nums = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, nums))
even = list(filter(lambda x: x % 2 == 0, nums))
sum_all = reduce(lambda a, b: a + b, nums)

print(squared)
print(even)
print(sum_all)
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))