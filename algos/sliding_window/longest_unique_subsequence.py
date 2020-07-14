"""
given a string find the longest unique subsequence

use the sliding window protocol
"""

def longest_unique_subsequence(substr):

    if len(substr) == 0:
        return 0

    lp = 0
    rp = 1
    longest = substr[0]
    ln_substr = len(substr)

    while rp < ln_substr:
        if substr[rp] in longest:
            if (rp - lp) > len(longest):
                longest = substr[lp:rp]
            for i in range(lp,rp):
                if substr[lp] == substr[i]:
                    lp = i+1
                    break
        elif rp == len(substr) - 1:
            if len(longest) < (rp - lp + 1):
                longest = substr[lp:rp + 1]
        rp += 1

    print (longest)
    return [lp,rp]
substr = 'kkkaxyk'
substr = 'kkkkkkkkkkkkk'
substr = '1231231231234'
lp,rp = longest_unique_subsequence(substr)
print (lp,'  ',rp)
