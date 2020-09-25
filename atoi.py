'''
String to Integer (atoi)

Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
'''
class Solution:
    def myAtoi(self, sut: str) -> int:
        if sut == '':
            return 0

        sut += 'a'
        ans = ''

        for i in range(len(sut)):
            if sut[i] == ' ':
                if ans:
                    break

                if sut[i + 1].isnumeric():
                    continue
                elif sut[i + 1] == ' ' or sut[i + 1] == '+' or sut[i + 1] == '-':
                    continue
                else:
                    break
            else:
                if sut[i].isnumeric():
                    ans += sut[i]
                else:
                    if sut[i] == '+' or sut[i] == '-':
                        if ans:
                            break

                        if sut[i + 1].isnumeric():
                            ans += sut[i]
                        else:
                            break
                    else:
                        break
        
        num = int(ans) if ans else 0
        
        if num >= (2 ** 31):
            return 2 ** 31 - 1
        elif num <= ((-1) * (2 ** 31)):
            return (-1) * (2 ** 31)
        else:
            return num

#Solution().myAtoi(' -42 0-1')
Solution().myAtoi('-91283472332')
