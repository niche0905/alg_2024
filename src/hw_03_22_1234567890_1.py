
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
    return ??? >= size

def new_bin():
    nb = []
    bins.append(nb)
    return nb

# 함수들을 채워라
def first_fit(size):
    for b in ???:
        if ???:
            return b
    return new_bin()

def next_fit(size):
    global last_bin
    if ???? and ????:
        return last_bin
    return new_bin()

def best_fit(size):
    smallest_bin = None
    smallest_size = BIN_SIZE
    ...

def worst_fit(size):
    largest_bin = None
    ...

fits = [ ... ]
for fit in fits:
    bins = []
    last_bin = None
    for num in nums:
        bin = first_fit(num)
        bin.append(num)
        last_bin = bin

    print(f'Function: <<first_fit>>')
    print(bins)
