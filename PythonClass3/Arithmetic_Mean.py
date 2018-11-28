def average(nums):
    mean = 0.0
    for num in nums:
        mean += num

    mean /= len(nums)

    return mean

##Another way of doing it
def average2(list):
    return sum(list) / len(list)


print(average([1, 5, 9]))

print(average(range(11)))

print(average(range(11)))
print(average(range(123)))
