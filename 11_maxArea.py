'''
11. Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
'''
class Solution:
    def maxArea(self, height) -> int:
        area = 0
        left_pos = 0
        right_pos = len(height) - 1
        
        while left_pos < right_pos:
            area = max(area, (min(height[left_pos], height[right_pos]) * (right_pos - left_pos)))

            if height[left_pos] < height[right_pos]:
                left_pos += 1
            else:
                right_pos -= 1

        return area
        

Solution().maxArea([1,8,6,2,5,4,8,3,7])
