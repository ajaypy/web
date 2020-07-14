"""
get next closest time from the digits in current time
"""

"""
get all the digits in current time
keep incrementing the time till the digits are in allowed
"""

def next_closest_time(ctime):

    cur = 60 * int(ctime[:2]) + int(ctime[3:])
    allowed = {int(x) for x in ctime if x != ':'}

    print (cur)
    print (allowed)
    print (cur % (24 * 60))

next_closest_time('12:34')





