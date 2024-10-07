from math import sqrt

coords = [
    (527, 416), (471, 625), (880, 13), (1163, 145), (1426, 806),
    (14, 429), (742, 531), (1037, 630), (1025, 879), (377, 257),
    (614, 553), (481, 676), (943, 53), (88, 9), (28, 271),
    (952, 279), (1426, 519), (699, 698), (925, 716), (1132, 414),
    (1371, 238), (1389, 689), (1573, 774), (915, 636), (941, 763),
    (1083, 385), (1297, 588), (764, 389), (1536, 186), (1098, 515),
    (1308, 65), (1111, 550), (566, 422), (124, 105), (620, 332),
    (784, 623), (182, 555), (1413, 451), (1092, 660), (30, 217),
    (525, 148), (1311, 887), (1228, 353), (54, 68), (1155, 838),
]

def dist(a, b):
    d = sqrt(dist_sq(a, b))
    return d

def dist_sq(a, b):
    d = (a[0]-b[0])**2 + (a[1]-b[1])**2
    return d

def brute_force(array, i1, i2):
    min_dist = float('inf')
    for x in range(i1, i2):
        for y in range(x+1, i2):
            d = dist_sq(array[x], array[y])
            if d < min_dist:
                min_dist = d
                s, e = x, y
    return s, e, sqrt(min_dist)

def dnc(array, i1, i2):
    size = i2 - i1 + 1
    if size <= 1:
        return -1, -1, 0
    elif size == 2:
        return i1, i2, dist(array[i1], array[i2])
    elif size == 3:
        return brute_force(array, i1, i2)

    # size >= 4

    last_left = (i1+i2) // 2
    s1, e1, d1 = dnc(array, i1, last_left)
    s2, e2, d2 = dnc(array, last_left+1, i2)

    if d1 <= d2:
        s, e, d = s1, e1, d1
    else:
        s, e, d = s2, e2, d2

    # strip
    x1 = last_left - d
    x2 = last_left + d
    index1 = min(t[2] for t in array if t[0] >= x1 and t[2] >= i1)# x 좌표가 x1 이상인 점들 중 가장 왼쪽 점의 인덱스
    index2 = max(t[2] for t in array if t[0] <= x2 and t[2] <= i2)# x 좌표가 x2 이하인 점들 중 가장 오른쪽 점의 인덱스

    strip = [t for t in y_aligned if index1 <= t[2] and t[2] <= index2]

    strip_length = len(strip)
    for x in range(strip_length):
        first = array[x]
        for y in range(x + 1, strip_length):
            second = array[y]
            y_diff = second[1] - first[1]
            if y_diff > d:
                break
            now_dist = dist(first, second)
            if d > now_dist:
                d = now_dist
                s, e = first[2], second[2]

    return s, e, d


print(coords)
coords.sort(key=lambda t:t[0])
x_aligned = [(coords[i][0], coords[i][1], i) for i in range(len(coords))]
print('--- x aligned ---')
print(x_aligned)
y_aligned = sorted(x_aligned, key=lambda t:t[1])
print('--- y aligned ---')
print(y_aligned)
# s, e, d = brute_force(coords, 0, len(coords) - 1) # 29, 30, 37.3363
s, e, d = dnc(x_aligned, 0, len(x_aligned) - 1) # 29, 30, 37.3363

# print(f'{s=} {e=} {d=}')
print(f'[{s}]{coords[s]} - [{e}]{coords[e]}, {d=}')
