the_list = [
        6,      82,      21,      58,      22,      54,      71,     215,      99,     227, 
       73,      24,      17,      44,     144,      78,      25,      66,      47,       3, 
       87,      33,     312,     242,      42,      61,     348,     346,      98,      92, 
       83,     100,      94,      40,       5,     458,     364,      26,      64,     735, 
       90,     489,      72,     504,      88,      97,     226,     218,     186,     168, 
]

count = len(the_list)


def sort_bubble(arr):
    print('-- Bubble', '-' * 60)
    print(f'before: {arr}')
    end = len(arr) - 1
    while end > 0:
        last = 1
        for i in range(end):
            if arr[i] > arr[i+1]:   # 교환 조건
                arr[i], arr[i+1] = arr[i+1], arr[i] # 교환
                last = i + 1    # 마지막 교환 장소 저장
        end = last - 1
    print(f'after : {len(arr)=}, {arr}')


def sort_select(arr):
    print('** Select', '*' * 60)
    print(f'before: {arr}')
    for i in range(count-1):
        findedMin = 99999   # 꽤 큰수로 설정
        for j in range(i, count):
            if findedMin > arr[j]:
                index = j   # 최소값 위치 저장
                findedMin = arr[j]  # 찾은 최소값 갱신
        arr[i], arr[index] = arr[index], arr[i] # 정렬되지 않은 맨 앞과 교환
    print(f'after : {len(arr)=}, {arr}')


def sort_insert(arr):
    print('== Insert', '=' * 60)
    print(f'before: {arr}')
    for i in range(1, count):   # 크기가 1인 배열은 정렬할 필요가 없다
        now = arr[i]    # 주인공 설정 - 나중에 교환 말고 대입을 하기위해 빼둠
        j = i - 1       # 주인공 바로 왼쪽부터 비교
        while j >= 0:
            if arr[j] > now:    # 주인공이 더 작다면 이동
                arr[j+1] = arr[j]
                j -= 1
            else:               # 더이상 비교할 필요가 없을 때 반복문 탈출
                break
        # 들어가야 할 위치 찾았으면 대입
        arr[j+1] = now  # 주인공 들어가야 할 위치로 대입
    print(f'after : {len(arr)=}, {arr}')


def sort_shell(arr):
    print('++ Shell', '+' * 60)
    print(f'before: {arr}')
    for gap in [31, 15, 7, 3, 1]:
        for start in range(gap, count): # 삽입정렬과 같이 맨 왼쪽 크기가 1 인 배열은 이미 정렬되어 있기에 0 패스하고 1 인덱스부터
            now = arr[start]    # 주인공 설정
            i = start - gap     # 주인공 왼쪽부터 gap 만큼 떨어진 친구와 비교
            while i >= 0:
                if arr[i] > now:    # 주인공 보다 크다면 주인공이 왼쪽으로 이동해야함
                    arr[i+gap] = arr[i]
                    i -= gap
                else:               # 비교할 필요가 없어지면 탈출
                    break
            arr[i+gap] = now
    print(f'after : {len(arr)=}, {arr}')


def main():
    sort_bubble(the_list[:])
    sort_insert(the_list[:])
    sort_select(the_list[:])
    sort_shell(the_list[:])


if __name__ == '__main__':
    main()
