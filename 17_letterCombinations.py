'''
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
'''
class Solution:
    def letterCombinations(self, digits: str):
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        if len(digits) < 1:
            return []

        output = phone[digits[0]]

        def combination(output, digits_dict):
            mix_list = []
            for i in range(len(output)):
                for j in range(len(digits_dict)):
                   mix_list.append(output[i] + digits_dict[j])
            return mix_list 

        cnt = 1
        while cnt < len(digits):
            output = combination(output, phone[digits[cnt]])
            cnt += 1
        
        return output

Solution().letterCombinations('29')
