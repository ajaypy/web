"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

init a heap with smallest element at top.
insert K elements
Then traverse the list comparing with the element at the top, 
if the new element is -
    smaller than the top, continue
    bigger than that at the top,remove the top and insert the new one 

    Time -
    adding an element in heap of size k . O(log k)
    as we do it for N elements, its O(N log k)
    Space -
    O(k)
"""
def findKthLargest( nums, k):
"""
:type nums: List[int]
:type k: int
:rtype: int
"""
return heapq.nlargest(k, nums)[-1]


