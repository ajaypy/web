"""
Given two sorted lists, find the median of the two

Given two lists A, B of length m, n
find i and j such that

i + j == (m - i) + (n - j) 
      or 
i + j == (m - i) + (n - j) + 1

such that
max (A[i-1],B[j-1]) <= min (A[i],B[j])
or 
A[i-1) < B[j] and B[j-1] < A[i]

where i = (m+n+1)/2 - j

max(A[i−1],B[j−1]),  when m + n is odd

(max(A[i−1],B[j−1])+min(A[i],B[j])) / 2 
when m+n is even


basically parallel binary search
"""

"""
A is the longer list
"""

def median (A,B):

    m,n = len(A), len(B)

    if m > n:
        A,B,m,n = B,A,n,m

    if n == 0:
        raise ValueError

    # traverse the smaller list
    imin,imax, half_len = 0,m,(m+n+1)/2

    while imin <= imax:
        # i is the index on A
        # j is the index on B
        i = (imin + imax) / 2
        j = half_len -  1

        if i < m and B[j-1] > A[i]:
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            imax = i - 1
        else:
                    # i is perfect

            if i == 0: 
                max_of_left = B[j-1]
            elif j == 0: 
                max_of_left = A[i-1]
            else: 
                max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: 
                min_of_right = B[j]
            elif j == n: 
                min_of_right = A[i]
            else: 
                min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0



