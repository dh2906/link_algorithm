import random
import time


def main():
    num = 1_000000
    s = []

    for value in range(num):
        s.append(random.randint(0, num))

    key = random.randint(0, num)

    start = time.time()
    location = sequential_search(s, key)
    end = time.time()

    #print(s)
    print("[Sequential Search Result]")
    print("Key value {0}: location {1}".format(key, location))
    print("Elapsed Time: {0:0.8f}ms".format((end - start) * 1_000))
    print()

    s.sort()

    start = time.time()
    location = binary_search(s, key)
    end = time.time()

    #print(s)
    print("[Binary Search Result]")
    print("Key value {0}: location {1}".format(key, location))
    print("Elapsed Time: {0:0.8f}ms".format((end - start) * 1_000))
    print()

    start = time.time()
    location = recursive_binary_search(s, key, 0, num - 1)
    end = time.time()

    #print(s)
    print("[Recursive Binary Search Result]")
    print("Key value {0}: location {1}".format(key, location))
    print("Elapsed Time: {0:0.8f}ms".format((end - start) * 1_000))
    print()

def sequential_search(s, key): # 순차 탐색
    num = len(s)
    location = 0

    while location < num:
        if s[location] == key:
            return location

        location += 1

    return -1


def binary_search(s, key): # 이진 탐색
    num = len(s)
    low = 0
    high = num - 1

    while low <= high:
        location = (high + low) // 2

        if s[location] == key:
            return location

        elif s[location] < key:
            low = location + 1

        else:
            high = location - 1

    # 코딩을 추가하세요.

    return -1


def recursive_binary_search(s, key, low, high): # 이진 재귀 탐색
    mid = round((low + high) / 2)

    # 코딩을 추가하세요.

    if low > high:
        return -1

    if s[mid] == key:
        return mid

    elif s[mid] < key:
        return recursive_binary_search(s, key, mid + 1, high)

    else:
        return recursive_binary_search(s, key, low, mid - 1)

if __name__ == "__main__":
    main()