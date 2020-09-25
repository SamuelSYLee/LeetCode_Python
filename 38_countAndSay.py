'''
38. Count and Say
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. 
Note: Each term of the sequence of integers will be represented as a string.
'''

class Solution:
    def countAndSay(self, n: int) -> str:
        base_dict = {1: '1'}
        if n > 1:
            for i in range(2, n + 1):
                prev_str = list(base_dict[i - 1])
                prev_str.append('0')
                say_str = ''
                cur = 0
                cnt = 1
                for j in range(1, len(prev_str)):
                    if prev_str[j] == prev_str[cur]:
                        cnt += 1
                    else:
                        say_str += str(cnt) + str(prev_str[j - 1])
                        cnt = 1
                    cur += 1

                base_dict[i] = say_str
            
        return base_dict[n]

Solution().countAndSay(10)
