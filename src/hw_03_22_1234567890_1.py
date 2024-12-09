
import random

random.seed('class_03_random_seed')
BIN_SIZE = 40
nums = [ random.randint(2, 9) for _ in range(20) ]
print(nums)

#bin = [ 1, 2, 3 ]
#bins = [ bin ]

def bin_free(bin):
    return BIN_SIZE - sum(bin)

def bin_can_hold(bin, size):
    return bin_free(bin) >= size

def new_bin():
    nb = []
    bins.append(nb)
    return nb

# 함수들을 채워라
def first_fit(size):
    for b in bins:
        if bin_can_hold(b, size):
            return b
    return new_bin()

def next_fit(size):
    global last_bin
    if last_bin != None and bin_can_hold(last_bin, size):
        return last_bin
    return new_bin()

def best_fit(size):
    smallest_bin = None
    smallest_size = BIN_SIZE
    for b in bins:
        binFree = bin_free(b)
        if smallest_size > binFree and binFree >= size:
            smallest_bin = b
            smallest_size = binFree
    if smallest_bin != None:
        return smallest_bin
    return new_bin()

def worst_fit(size):
    largest_bin = None
    largest_size = -1
    for b in bins:
        binFree = bin_free(b)
        if largest_size < binFree and binFree >= size:
            largest_bin = b
            largest_size = binFree
    if largest_bin != None:
        return largest_bin
    return new_bin()

fits = [ first_fit, next_fit, best_fit, worst_fit ]
outString = ["first_fit", "next_fit", "best_fit", "worst_fit"]
for i, fit in enumerate(fits):
    bins = []
    last_bin = None
    for num in nums:
        bin = fit(num)
        bin.append(num)
        last_bin = bin

    print(f'Function: <{outString[i]}>')
    print(bins)
