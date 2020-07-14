"""
given a licese key with alphanumeric characters and dashes.
given a value K, divide it into portions haing K characters each

case 1: length < K
case 2: length = n * K ( n>=1)
case 3: length != n * K ( n>=1)

tests:
    0 length
    length < K
    K = 1
    K = 2
    K = 3
    K = 0
"""

def lic_key_formatting(S,K):
    nd = ''.join(S.split('-'))
    nd = nd.lower()

    l_nd = len(nd)

    ret_str = ''
    if l_nd == 0 or K == 0:
        return ''

    s_i = l_nd % K
    print (nd)
    print (l_nd,s_i)

    if l_nd <= K:
        return nd

    if s_i > 0:
        ret_str = ''.join(nd[:s_i]) + '-'
        print (ret_str)
    e_i = s_i + K
    while e_i <= l_nd:
        ret_str = ret_str + ''.join(nd[s_i:e_i]) + '-'
        s_i = e_i
        e_i += K
        print (ret_str)
    return ret_str.strip('-')


lic_key = "5F3Z-2eZ-9-w-7865543"
lic_key = ""
print (lic_key_formatting(lic_key,0))

