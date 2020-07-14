"""
There is a stack of integers and a queue of integers
perform following operations

#1. Pop the elements from the stack and push them to the queue, untill the stack is empty

#2. Push the current array elements on top of the stack

#3. Pop element from the queue and push on to the stack
"""

def st_queue():

    st = []
    lst = [1,2,3,4,5,6,7,8,9,10]
    qu = []

    for ele in lst:
        #1.
        while len(st):
            qu.append(st.pop())

        st.append(ele)

        while len(qu):
            st.append(qu.pop(0))
        print ("st =", st)
        print ("qu =", qu)

    print ("st =", st)
    print ("lst =", lst)
    print ("qu =", qu)


st_queue()
print ("-------------------- ---------------------")

from collections import deque

def st_queue_dq():

    st = deque()
    qu = deque()
    lst = [1,2,3,4,5,6,7,8,9,10]

    for ele in lst:
        #1.
        while len(st):
            qu.append(st.pop())

        st.append(ele)

        while len(qu):
            st.append(qu.popleft())
        print ("st =", st)
        print ("qu =", qu)

    print ("st =", st)
    print ("lst =", lst)
    print ("qu =", qu)
    print ("locals =", locals())

st_queue_dq()

