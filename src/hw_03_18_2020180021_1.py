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

roots = [n for n in range(num_vertex)]
# edges = []

# 튜플을 담는다 n-1 (n은 정점의 개수)
mst = []

def append(s, e, w):    # 과제 검수용 (건드리지 말것)
    if s <= e:
        mst.append((s,e,w))
    else:
        mst.append((e,s,w))
    mst.sort(key=lambda e:e[0]*1000+e[1])
def spanning(): # mst가 n-1이면 다 확장한 상황이다
    return len(mst) >= num_vertex - 1
def onSameTree(u, v):   # 부모가 같은지 (사이클 확인용)
    return getRoot(u) == getRoot(v)

def getRoot(v): # root를 구하는 함수 key와 value가 같을 때까지 재귀
    if v != roots[v]:
        roots[v] = getRoot(roots[v])
    return roots[v]

def connect(u, v):  # 서로 연결되는지를 알 수 있다 (기존 union)
    u_root = getRoot(u)
    v_root = getRoot(v)
    if u_root > v_root:
        u_root, v_root = v_root, u_root
    roots[v_root] = u_root

edges.sort(key=lambda e: e[2])    # 가중치로 정렬

for s,e,w in edges:
    if spanning(): break
    if onSameTree(s, e): continue
    connect(s, e)
    # mst.append((s, e, w))
    append(s, e, w)

print(mst)
