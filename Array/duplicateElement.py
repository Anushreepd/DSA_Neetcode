def duplicateElement(arr):
    element_list = []
    duplicate_list = []
    for i in range(len(arr)):
        if arr[i] in element_list:
            duplicate_list.append(arr[i])
        else :
            element_list.append(arr[i])
    return duplicate_list

arr = [1,2,3,4,1,2,3]
print("Duplicates", duplicateElement(arr))