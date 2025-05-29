import time
import sys

dp = None

def main():
    num = 10000

    global dp
    dp = [None for _ in range(num + 1)]

    start = time.time()
    result1 = iterative_fibonacci(num)
    end = time.time()

    print("[Iterative Fibonacci]")
    print("Num {0} : Fibonacci Number {1}".format(num, result1))
    print("Elapsed Time: {0:08f}s".format((end - start)))
    print()

    start = time.time()
    result2 = recursive_fibonacci(num)
    end = time.time()

    print("[Recursive Fibonacci]")
    print("Num {0} : Fibonacci Number {1}".format(num, result2))
    print("Elapsed Time: {0:08f}s".format((end - start)))
    print()


def iterative_fibonacci(num): # 0번째부터 피보나치가 시작된다 가정
    if num <= 1:
        return num

    num1, num2 = 0, 1

    for i in range(2, num + 1):
        num1, num2 = num2, num1 + num2

    return num2



def recursive_fibonacci(num):
    global dp

    if num <= 1:
        return num

    if dp[num] is None:
        dp[num] = recursive_fibonacci(num - 1) + recursive_fibonacci(num - 2)

    return dp[num]



if __name__ == "__main__":
    main()
