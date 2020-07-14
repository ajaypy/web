"""
Find the longest repeated substring using Suffix Array
"""

S = "ABRACADABRA"

def get_repeated_substring_with_suffix_array(S):

    N = len(S)
    sa_map = {}
    lcp_map = {}

    for i in range(N):
        sa_map[S[i:]] = i
    sorted_keys = sorted(sa_map.keys())
    print (sorted_keys)
    print (len(sorted_keys))
    lcp_map[sorted_keys[0]] = 0
    for i in range(1,len(sorted_keys)):
        max_count = min(len(sorted_keys[i-1]), len(sorted_keys[i]))
        lcp_map[sorted_keys[i]] = 0
        for count in range(max_count):
            if sorted_keys[i-1][count] == sorted_keys[i][count]:
                lcp_map[sorted_keys[i]] += 1
    print (sa_map)
    print (sorted_keys)
    for k,v in lcp_map.items():
        print (k,v)



get_repeated_substring_with_suffix_array(S)
