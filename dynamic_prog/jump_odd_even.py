"""
Given an integer array A.  From some starting index, you can make a series of jumps.  The (1st, 3rd, 5th, ...) jumps in the series are called odd numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even numbered jumps.

You may from index i jump forward to index j (with i < j) in the following way:

During odd numbered jumps (ie. jumps 1, 3, 5, ...), you jump to the index j such that A[i] <= A[j] and A[j] is the smallest possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
During even numbered jumps (ie. jumps 2, 4, 6, ...), you jump to the index j such that A[i] >= A[j] and A[j] is the largest possible value.  If there are multiple such indexes j, you can only jump to the smallest such index j.
(It may be the case that for some index i, there are no legal jumps.)
A starting index is good if, starting from that index, you can reach the end of the array (index A.length - 1) by jumping some number of times (possibly 0 or more than once.)
"""


"""
DYNAMIC PROGRAMING WORKS
#1. we have a known solution
#2. the jumps can only be forward, if the jumps can be random, this won't work
#3. If the jumps are random, then its a problem of finding loops. Keep an array of visited indexes and failed indexes. Still a dynamic programming but start from left in that case

"""
#input
A = [16,10,13,12,11,14,15,9]
N = len(A)

#input value to key map
ad = {}
for i,v in enumerate(A):
    ad[v] = i

index_count = 1

#method to get the next highest 
def get_next_higher(n,R):

    high = float("inf")
    for x in R:
        if x > n and x < high:
            high = x

    if high == n or high == float("inf"):
        return None
    return high

#method to get the next lowest 
def get_next_lower(n,R):

    low = float("-inf")
    for x in R:
        if x < n and x > low:
            low = x

    if (low == n) or (low == float("-inf")):
        return None
    return low

# SOLUTION 1. START FROM END
# non Recursive, dynamic programming

# arrays to check the validity of the jumps
lower  = [False]*N
higher = [False]*N

# set the condition that last index is always valid
lower[-1] = True
higher[-1] = True

# array to store the processed indexes
R = []
R.append(A[-1])

for i in range(N-2,0,-1):

    cur = A[i]
    high = get_next_higher(cur,R)
    low = get_next_lower(cur,R)


    if high:
        higher[i] = lower[ad[high]]

    if low:
        lower[i] = higher[ad[low]]

    R.append(A[i])

    if higher[i]:
       index_count += 1


print ("Total Indexes:", index_count)
print ("Valid Indexes:", [x for x,v in enumerate(higher) if v])

# SOLUTION 2. START FROM BEGIN
# RECURSIVE, not dynamic
R = []
RE = []
RO = []



def get_index_status(jump,cur_index,A,RE,RO):

    print ("jump=%r :cur_index=%r :array=%r"%(jump,cur_index,A))
    print ("RE=%r :RO=%r "%(RE,RO))
    if (jump % 2):
        #odd jump
        if cur_index in RO:
            return True
        next_value = get_next_higher(A[cur_index],A[cur_index+1:])
    else:
        #even jump
        if cur_index in RE:
            return True
        next_value = get_next_lower(A[cur_index],A[cur_index+1:])

    if next_value:
        next_index = ad[next_value]
        if next_index == N-1:
            return True
        return get_index_status(jump+1,next_index,A,RE,RO)
    return False


for i in range(N-1):
    if i in RO:
        R.append(i)
        continue
    print ("ITERATION= :", i)
    if get_index_status(1,i,A,RE,RO):
        R.append(i)

R.append(N-1)
print ("REC: ", R)

