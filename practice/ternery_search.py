import random
import time

def ternary_search(lst, target, left, right):
    if left > right: # 타겟 존재하지 않는 경우
        return -1

    third = (right - left) // 3 # 리스트를 3등분 하기 위한 계산
    mid1 = left + third
    mid2 = right - third

    if lst[mid1] == target: # 탐색 성공 시 종료
        return mid1
    elif lst[mid2] == target: # 탐색 성공 시 종료
        return mid2

    if target < lst[mid1]: # 타겟이 3등분 기준 왼쪽 구간 범위에 있는 경우
        return ternary_search(lst, target, left, mid1 - 1)

    elif target > lst[mid2]: # 타겟이 3등분 기준 오른쪽 구간 범위에 있는 경우
        return ternary_search(lst, target, mid2 + 1, right)

    else: # 타겟이 3등분 기준 가운데 구간 범위에 있는 경우
        return ternary_search(lst, target, mid1 + 1, mid2 - 1)

if __name__ == "__main__":
    s = []
    n = 10000000
    target = 10

    for i in range(n):
        s.append(random.randint(0, n))

    s.sort()

    start = time.process_time()
    idx = ternary_search(s, target, 0, len(s) - 1)
    end = time.process_time()
    print("[Search Result]")
    print("위치 :", idx if idx != -1 else "탐색 실패")
    print("Elapsed Time: {0:0.4f}s".format(end - start))