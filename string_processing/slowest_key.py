"""
find the slowest key based on the time taken to press it
"""
def get_slowest_key(K):
    slowest_key = K[0][0]
    slowest_time = K[0][1]
     
    print (slowest_key, " ; ", slowest_time)
    for i in range(1, len(K)):
         if K[i][1] - K[i-1][1] > slowest_time:
             slowest_key = K[i][0]
             slowest_time = K[i][1] - K[i-1][1]


    return slowest_key



kT = [[0,2],[1,5],[0,9],[2,15],[4,19],[3,29],[0,41],[1,45]]
print (get_slowest_key(kT))



