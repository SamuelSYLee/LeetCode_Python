'''
28. Implement strStr()
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        else:
            try :
                return haystack.index(needle)
            except:
                return -1

Solution().strStr('aaa', 'ba')
