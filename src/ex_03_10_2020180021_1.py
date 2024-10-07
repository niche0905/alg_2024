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

def insertionSort(arr, left, right): #right = inclusive
    for i in range(left+1, right+1):
        juin = arr[i]
        j = i-1
        while j >= left and arr[j] > juin:  # 옮긴다
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = juin

def mergeSort(arr, start, end): # end = inclusive
    size = (end-start) + 1
    if size <= 5:
        insertionSort(arr, start, end)
        return

    last_left = (start+end) // 2
    mergeSort(arr, start, last_left)
    mergeSort(arr, last_left+1, end)
    merge(arr, start, last_left, end)

def merge(arr, start, last_left, end): # end = inclusive
    # left_array = arr[start:last_left+1]
    # right_array = arr[last_left+1, end+1]
    merged = []
    l = start
    r = last_left+1
    while l <= last_left and r <= end:
        if arr[l] <= arr[r]:
            merged.append(arr[l])
            l += 1
        else:
            merged.append(arr[r])
            r += 1

    while l <= last_left:
        merged.append(arr[l])
        l += 1

    while r <= end:
        merged.append(arr[r])
        r += 1

    arr[start:end+1] = merged


mergeSort(words, 0, len(words)-1)
print(words)
