edges=[
    (0, 6, 343), (0, 21, 494), (0, 22, 303), (1, 5, 438), (1, 13, 221), 
    (1, 20, 465), (2, 14, 411), (2, 18, 66), (2, 19, 33), (2, 23, 479), 
    (3, 9, 150), (3, 17, 158), (3, 21, 457), (4, 14, 214), (4, 15, 305), 
    (4, 18, 509), (4, 22, 519), (4, 23, 157), (4, 24, 356), (5, 7, 286), 
    (5, 12, 481), (5, 13, 230), (5, 16, 439), (5, 17, 383), (5, 20, 199), 
    (6, 12, 516), (6, 15, 355), (6, 18, 492), (6, 19, 518), (6, 22, 256), 
    (6, 24, 306), (7, 11, 156), (7, 19, 486), (8, 12, 508), (8, 16, 373), 
    (8, 17, 203), (9, 10, 225), (9, 16, 413), (9, 17, 295), (10, 16, 213), 
    (10, 21, 358), (11, 13, 138), (11, 20, 193), (12, 13, 269), (12, 16, 135), 
    (13, 20, 327), (14, 15, 370), (14, 18, 345), (14, 19, 435), (14, 24, 348), 
    (15, 23, 373), (16, 21, 262), (17, 21, 437), (22, 24, 282), (23, 24, 374)
]
num_vertex = 25

start = 8

# edge list 형태의 입력을 Adjacency Matrix (List) 형태로 변환
g = { s: dict() for s in range(num_vertex) }
for s,e,w in edges:
    # pass # 채워 넣으세요
    g[s][e] = w
    g[e][s] = w


from heapdict import heapdict
mst = [] # 결과물이 tree 형태로 저장될 예정
D = heapdict()     # 알려진 거리들 저장. key 까지 가는 비용은 value 임.
origins = dict()   # key 까지 가려면 value 에서 가야 한다는 정보 저장
completed = set()  # 내륙에 속하는 점들을 모아 둔다

def append(s, e, w):
    if s <= e:
        mst.append((s,e,w))
    else:
        mst.append((e,s,w))
    mst.sort(key=lambda e:e[0]*1000+e[1])

def update(s, e, w):
    if e in completed: return     # 내륙이면 무시
    if e in D.keys() and D[e] <= w: return # 존재하고 기존게 싸면 무시

    # D 및 origins 를 갱신한다.
    D[e] = w
    origins[e] = s

# 시작점에 대한 정보를 저장하고 메인 루프에 들어간다
D[start] = 0
origins[start] = start

while D: # 알려진 거리정보가 남아 있는 동안
# while len(completed) < num_vertex:
# while len(mst) < num_vertex-1:
    to_vertex, weight = D.popitem()
    fr_vertex = origins[to_vertex]
    completed.add(to_vertex)
    if fr_vertex != to_vertex:   # 맨 처음이면 (from과 to가 같으면)
        append(to_vertex, fr_vertex, weight)
    for adj, adj_w in g[to_vertex].items():
        update(to_vertex, adj, adj_w)

print(mst)

# print paths for homework *_3.py
# 다익스트라를 위한 것

# def path_to(to):
#     fr = origins[to]
#     if fr == to: return 0, f'{to}'
#     cost, path = path_to(fr)
#     return cost + ????, ????

# for to in range(num_vertex):
#     cost, path = path_to(to)
#     print(f'{path=} {cost=}')
