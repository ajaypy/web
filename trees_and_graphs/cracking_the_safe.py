"""
There is a box protected by a password. The password is a sequence of n digits where each digit can be one of the first k digits 0, 1, ..., k-1.

While entering a password, the last n digits entered will automatically be matched against the correct password.

For example, assuming the correct password is "345", if you type "012345", the box will open because the correct password matches the suffix of the entered password.
"""

def crack_safe_1(n,k):

    seen = set()
    ans = []

    def dfs(node):
        for x in map(str,range(k)):
            nei = node + x
            print ("Node: %r,  Nei: %r" % (node, nei))
            if nei not in seen:
                seen.add(nei)
                dfs(nei[1:])
                ans.append(x)
    dfs("0" * (n-1))
    return "".join(ans) + "0"* (n-1)

n = 2
k = 2

passwd = crack_safe_1(n,k)
print (passwd)

