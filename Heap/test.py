def pairing_problem(arr_a, k):
    arr_b = []
    for i in range(1,len(arr)+1):
        for j in range(i+2, len(arr)+1):
            arr_b.append(abs(arr[i]-arr[j]))
    return sorted(arr_b)[k]

arr = [1,7, 9, 4, 5]
k = 4
print (pairing_problem(arr,k))