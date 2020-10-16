'''
29. Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.
'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        flag = (dividend < 0) ^ (divisor < 0)
        answer = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend < divisor:
            return 0

        def approximate(dividend, divisor, answer):
            appr = divisor
            cnt = 1

            while appr <= dividend:
                prev_appr = appr
                prev_cnt = cnt
                appr += appr
                cnt += cnt
            
            answer += prev_cnt
            residual = dividend - prev_appr
            if residual >= divisor:
                residual, answer = approximate(residual, divisor, answer)
            return residual, answer
            
        residual, answer = approximate(dividend, divisor, answer)
        return max(-2 ** 31, -answer) if flag else min(2 ** 31 - 1, answer)

Solution().divide(-2147483648, -1)
