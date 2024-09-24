
words = [
  '2020180021', 'hut', 'apostle', 'equipment', 'fop', 'refined', 'parapet', 'mog', 'amputate', 'covetous', 'somebody',
  'all', 'lobbyist', 'remark', 'subscriber', 'quorum', 'steppe', 'clean', 'cu', 'commend', 'prosy',
  'supererogation', 'indignation', 'wolverine', 'emporium', 'intersect', 'constitution', 'miscast', 'rabbi', 'enmity', 'loft',
  'temporize', 'speedboat', 'agenda', 'delusion', 'addle', 'idolize', 'romance', 'overestimate', 'revive', 'smell',
  'quite', 'seminar', 'bloomers', 'lives', 'innocuous', 'effluent', 'cross', 'recidivist', 'wet', 'synth',
  'mantilla', 'tweak', 'lowbrow', 'aviation', 'quadruped', 'capable', 'graphic', 'barman', 'intemperate', 'mastermind',
  'submit', 'considering', 'riddance', 'polyethene', 'jim', 'varicolored', 'medic', 'ferric', 'minaret', 'capacitor',
  'pusher', 'gingerbread', 'grizzled', 'upsilon', 'km', 'glade', 'ribbon', 'parascending', 'shinty', 'breve',
  'hotel', 'similitude', 'fuddle', 'secretariat', 'silicate', 'whinchat', 'abstention', 'untrue', 'toing', 'cnd',
  'ramification', 'scorn', 'apricot', 'arnica', 'militate', 'muslim', 'homicide', 'overfeed', 'shooting', 'growth',
]

count = len(words)


def down_head(arr, root, size):
    leftChild = root * 2 + 1
    if leftChild >= size:   # 올바른 인덱스가 아님으로
        return
    child = leftChild
    rightChild = root * 2 + 2
    if rightChild < size:   # 오른 자식이 있다면 비교
        if arr[leftChild] < arr[rightChild]:    # 오른 자식이 더 크다면 비교할 자식 교체
            child = rightChild

    if arr[root] < arr[child]:  # 부모가 자식보다 작다면 바꾸어야 함
        arr[root]. arr[child] = arr[child], arr[root]
        down_head(arr, child, size) # 교체 시 자식 노드들의 힙 구조가 망가졌을 수도 있으니 재귀 호출


def head_sort(arr):
    global count
    print('-- head', '-' * 60)
    print(f'before: {arr}')
    lastParentIndex = count // 2 - 1    # 부모 노드중 가장 큰 인덱스
    print(f'after : {len(arr)=}, {arr}')


def main():
    head_sort(words[:])


if __name__ == 'main':
    main()