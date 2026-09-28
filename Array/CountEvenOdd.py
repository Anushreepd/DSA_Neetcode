def CountEvenOrOdd(arr):
    even = 0
    odd = 0
    for i in range(len(arr) - 1):
        if arr[i] % 2 == 0 :
            even = even + 1
        else:
            odd = odd + 1

    return even, odd

arr = [1,3,4,6,8,91,6]
even, odd = CountEvenOrOdd(arr)
print("Even count=", even, "odd =", odd)