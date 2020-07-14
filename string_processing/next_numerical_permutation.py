"""
given a number find the next smallest greater number

123 -> 321
321 -> 123
115 -> 151

advance from the units place as long as its increasing
when reach the first position which is decrementing, swap it with the
next higher number

then reverse all the numbers to the right of the swapped
"""

class Solution:
    def __init__(self, num):
        self.num = str(num)

    def get_next_permutation(self):
        num = self.num
        if num == '' or num == '0':
            return 0

        num_len = len(num)
        low_p = -1
        for i in range(num_len-2,-1,-1):
            print ( i, ':',num[i], ':', num[i+1])
            if int(num[i]) < int(num[i+1]):
                continue
            low_p = i-1
            break

        print (low_p)
        if low_p != -1:
            i = num_len -1
            while (i >= 0) and (num[i] < num[low_p]):
                print (num[low_p]," : ", num[i])
                i -= 1

            print (num[low_p]," : ", num[i])
            if i > low_p:
                num_l = list(num)
                num_l[i], num_l[low_p] = num_l[low_p],num_l[i]
                num = ''.join(num_l)
                print (num)

                num1 = num[:i+1]
                num2 = num[i+1:]
                print (num1, num2)
                num = num1 + num2[::-1]
        return num

s = Solution('127534')
print (s.get_next_permutation())
