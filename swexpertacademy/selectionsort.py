def selection_sort(arr, num):
    if (num == 1):
        minNum = min(arr)
        arr[arr.index(minNum)] = arr[0]
        arr[0] = minNum

    elif (num == len(arr)):
        return arr

    else:
        minNum = min(arr[num:])
        arr[arr.index(minNum)] = arr[num - 1]
        arr[num - 1] = minNum
        selection_sort(arr, num + 1)
