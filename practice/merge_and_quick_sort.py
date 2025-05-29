import random
import time




def main():


    ###################
    #   Create List   #
    ###################
    LEN = 100000

    n = LEN
    s = []


    for i in range(n):
        s.append(random.randint(0, n))


    s1 = s.copy()
    s2 = s.copy()
    s.sort()


    # print("s1:", s1)  # merge sort
    # print("s2:", s2)  # quick sort
    # print()


    ##################
    #   Merge Sort   #
    ##################


    start = time.perf_counter()
    merge_sort(s=s1, low=0, high=len(s2) - 1)
    end = time.perf_counter()
    print("[Merge Sort Result]")
    print("Elapsed Time: {0:0.4f}ms".format((end - start) * 1_000))
    print("s1:", s1)
    print("Correct:", s == s1)
    print()


    ##################
    #   Quick Sort   #
    ##################


    start = time.perf_counter()
    quick_sort(s=s2, low=0, high=len(s2) - 1)
    end = time.perf_counter()
    print("[Quick Sort Result]")
    print("Elapsed Time: {0:0.4f}ms".format((end - start) * 1_000))
    print("s2:", s2)
    print("Correct:", s == s2)
    print()


    #############
    #   TRIAL   #
    #############


    TRIAL = 20
    total_elapsed_time_merge_sort = 0
    total_elapsed_time_quick_sort = 0


    print("[progressing] - TRIAL: {}".format(TRIAL))
    print(">" * (TRIAL // (TRIAL // 20)))


    for trial in range(TRIAL):
        # Create list
        n = LEN
        s = []
        for i in range(n):
            s.append(random.randint(0, n))


        s1 = s.copy()
        s2 = s.copy()


        # Merge Sort
        start = time.perf_counter()
        merge_sort(s=s1, low=0, high=len(s2) - 1)
        end = time.perf_counter()
        total_elapsed_time_merge_sort += end - start


        # Quick Sort
        start = time.perf_counter()
        quick_sort(s=s2, low=0, high=len(s2) - 1)
        end = time.perf_counter()
        total_elapsed_time_quick_sort += end - start


        if TRIAL >= 20 and (trial + 1) % (TRIAL // 20) == 0:
            print(">", end="", flush=True)


    print()
    print("Merge Sort - Elapsed Time: {:.5}s".format(total_elapsed_time_merge_sort))
    print("Quick Sort - Elapsed Time: {:.5}s".format(total_elapsed_time_quick_sort))




def merge_sort(s, low, high):
    if low < high: # 시작점이 끝점을 넘어가지 않는 선에서 재귀
        mid = (low + high) // 2
        merge_sort(s, low, mid) # 시작 ~ 중간까지 분할
        merge_sort(s, mid + 1, high) # 중간 + 1 ~ 끝까지 분할
        merge(s, low, mid, high) # 나눈 리스트를 병합




def merge(s, low, mid, high):
    tmp = [0] * (high - low + 1) # 정렬 결과를 임시로 저장하는 리스트
    i = low
    j = mid + 1
    t = 0

    while i <= mid and j <= high:
        if s[i] <= s[j]: # 왼쪽 리스트의 요소가 더 작으면 임시 리스트에 저장
            tmp[t] = s[i]
            i += 1 # 다음 요소로 이동

        else: # 오른쪽 리스트의 요소가 더 작으면 임시 리스트에 저장
            tmp[t] = s[j]
            j += 1 # 다음 요소로 이동

        t += 1 # 임시 리스트의 저장 인덱스 증가

    while i <= mid: # 왼쪽 리스트의 요소가 아직 남은 경우 모두 넣기
        tmp[t] = s[i]
        t += 1
        i += 1

    while j <= high: # 오른쪽 리스트의 요소가 아직 남은 경우 모두 넣기
        tmp[t] = s[j]
        t += 1
        j += 1

    t = 0
    i = low

    while i <= high: # 임시 리스트의 결과 덮어쓰기
        s[i] = tmp[t]
        i += 1
        t += 1


def quick_sort(s, low, high):
    if low < high:
        pivot = partition(s, low, high)
        quick_sort(s, low, pivot - 1)
        quick_sort(s, pivot + 1, high)

def partition(s, low, high):
    x = s[high]
    i = low - 1


    # 코딩을 추가하세요.
    for j in range(low, high):
        if (s[j] < x):
            i += 1
            s[i], s[j] = s[j], s[i]

    s[i+1], s[high] = s[high], s[i+1]

    return i + 1




if __name__ == "__main__":
    main()
