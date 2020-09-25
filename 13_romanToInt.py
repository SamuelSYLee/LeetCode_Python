'''
13. Roman to Integer
Given a roman numeral, convert it to an integer. 
Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        rom_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'z': 0}
        lst = list(s)
        num = 0
        for i in range(1, len(lst)):
            if ((lst[i - 1] == 'I' and (lst[i] == 'V' or lst[i] == 'X')) or 
            (lst[i - 1] == 'X' and (lst[i] == 'L' or lst[i] == 'C')) or
            (lst[i - 1] == 'C' and (lst[i] == 'D' or lst[i] == 'M'))):
                num += (rom_dict[lst[i]] - rom_dict[lst[i - 1]])
                lst[i] = 'z'
                lst[i - 1] = 'z'

        for i in range(0, len(lst)):
            num += rom_dict[lst[i]]
        
        return num 

Solution().romanToInt('LXXXVIII')
