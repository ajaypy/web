"""
bubble
"""

def bubble_sort(arr):

    print (arr)
    N = len(arr)

    for i in range(N):
        for j in range(i+1,N):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j],arr[i]


    print (arr)

def selection_sort(arr):

    print (arr)
    N = len(arr)
    for i in range(N):
        minimum = i
        for j in range(i+1,N):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum],arr[i] = arr[i],arr[minimum]
        print (arr)
    print (arr)

#A = [7,4,5,2]
#bubble_sort(A)

A = [102,17,27,6,12,17,7,7,4,5,2,19,21,44,1,3,10,11,101,0]
bubble_sort(A)
print ("----------------- -----------------")
A = [102,17,27,6,12,17,7,7,4,5,2,19,21,44,1,3,10,11,101,0]
selection_sort(A)

def merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1



