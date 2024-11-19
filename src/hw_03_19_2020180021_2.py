d = [2, 5, 9, 7, 3, 9, 4, 6, 2, 7]


mc = len(d) - 1

INF = float('inf')

C = [[0 for _ in range(mc+1)] for _ in range(mc+1)]
P = [[0 for _ in range(mc+1)] for _ in range(mc+1)]
# p[b][e] = k 는 b 부터 e 까지 곱할 때
# 최종 곱셈을 k 직후에 한다는 뜻

for sps in range(2, mc+1):     # sub_problem_size
    spc = mc - sps + 1         # sub_problem_count
    for beg in range(1, spc+1):
        end = beg + sps - 1
        # C[beg][end] = ???
        C[beg][end] = INF
        for k in range(beg, end):
            t = C[beg][k] + C[k+1][end] + d[beg-1]*d[k]*d[end]
            if t < C[beg][end]:
                C[beg][end] = t
                P[beg][end] = k

def path(i, j):
    if i == j:
        return f'A{i}'

    p = P[i][j]
    return f'({path(i,p)}x{path(p+1,j)})'

print(path(1, mc), C[1][mc])