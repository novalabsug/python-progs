def get_largest_numbers (numbers, n):
    numbers.sort()

    return numbers[-n:]

nums = [2,3,4,1,34,123,321,1]

print(nums)
largest = get_largest_numbers(nums, 2)
print(nums)