def FirstRepeatingCharacter(arr):
    seen = set()
    for i in arr:
        if i in seen:
            return i
        seen.add(i)
    return None
arr = [1,1,2,4,2,2,9,9,8,8]
print(FirstRepeatingCharacter(arr))