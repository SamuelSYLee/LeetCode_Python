'''
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.
'''
class Solution:
    def reverse(self, x) -> int:
        if x == 0 or x == '' or x >= (2 ** 31) or x < ((-1) * (2 ** 31)):
            return 0
        else:
            x_lst = list(str(abs(x)))
            if x_lst[-1] == '0':
                x_lst.pop(-1)
            
            x_lst.reverse()
            if x < 0:
                x_rev = (-1) * int("".join(x_lst))
                if x_rev < ((-1) * (2 ** 31)):
                    return 0
                else:
                    return x_rev
            else:
                x_rev =  int("".join(x_lst))
                if x_rev >= (2 ** 31):
                    return 0
                else:
                    return x_rev

Solution().reverse(1563412)
