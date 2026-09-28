arr = [1,2,3,4]
arr.reverse()
print("reverse of array", arr)
print("reverse of array", arr[:: -1])

def reverse(arr):
    left = arr[0]
    right = len(arr)

    while left < right:
        arr[left],arr[right] = arr[right], arr[left]
        left = left + 1
        right = right -1

    return arr

print("reverse", reverse(arr))
