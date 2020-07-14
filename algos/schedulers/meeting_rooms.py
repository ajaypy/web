"""
Given a meeting schedule, find the minimum number of rooms needed to schdule all of them.


https://leetcode.com/articles/meeting-rooms-ii/
"""


#1. Priority Queues
"""
sort by time. At beginning of meeting find an available room.

rather than rotating round-robin to find an empty room
put the rooms in a heap with ending time as key and min-end-time at
the top.
1. Sort the given meetings by their start time.
2. Initialize a new min-heap and add the first meeting's ending time to the heap. We simply need to keep track of the ending times as that tells us when a meeting room will get free.
3. For every meeting room check if the minimum element of the heap i.e. the room at the top of the heap is free or not.
4. If the room is free, then we extract the topmost element and add it back with the ending time of the current meeting we are processing.
5. If not, then we allocate a new room and add it to the heap.
6. After processing all the meetings, the size of the heap will tell us the number of rooms allocated. This will be the minimum number of rooms needed to accommodate all the meetings.

"""

def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    free_rooms = []

    intervals.sort(key=lambda x: x[0])
    heapq.heapqpush(free_rooms,intervals[0][1])


#2. Sorted arrays
"""
if no room has an endtime earlier than the meting start time, than that 
meeting will need a new meeting room

In place of Heap
use two arrays
arr1 : sorted by start time, to pick the meeting
arr2 : sorted by end time, to pick the room

1. Separate out the start times and the end times in their separate arrays.
2. Sort the start times and the end times separately. Note that this will mess up the original correspondence of start times and end times. They will be treated individually now.
3. We consider two pointers: s_ptr and e_ptr which refer to start pointer and end pointer. The start pointer simply iterates over all the meetings and the end pointer helps us track if a meeting has ended and if we can reuse a room.
4. When considering a specific meeting pointed to by s_ptr, we check if this start timing is greater than the meeting pointed to by e_ptr. If this is the case then that would mean some meeting has ended by the time the meeting at s_ptr had to start. So we can reuse one of the rooms. Otherwise, we have to allocate a new room.
5. If a meeting has indeed ended i.e. if start[s_ptr] >= end[e_ptr], then we increment e_ptr.
6. Repeat this process until s_ptr processes all of the meetings.
"""
def min_meeting_rooms_no_heap(intervals):

    used_rooms = 0

    s_time = sorted([i[0] for i in intervals])
    e_time = sorted([i[1] for i in intervals])

    L = len(intervals)

    s_p = 0
    e_p = 0

    while s_p < L:
        if s_time[s_p] >= e_time[e_p]:
            used_rooms -= 1
            e_p += 1
        used_rooms += 1
        s_p += 1


    return used_rooms

intervals = [(1, 10), (2, 7), (3, 19), (8, 12), (10, 20), (11, 30)]
print (min_meeting_rooms_no_heap(intervals))
