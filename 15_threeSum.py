'''
15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.
'''
class Solution:
    def threeSum(self, nums):
        target_list = []

        if len(nums) < 3:
            return target_list
        
        nums.sort()

        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                j = i + 1
                k = len(nums) - 1

                while j < k:
                    target = nums[i] + nums[j] + nums[k]
                    
                    if target == 0:
                        target_list.append([nums[i], nums[j], nums[k]])

                        while j < k and nums[j] == nums[j + 1]:
                            j += 1
                        while j < k and nums[k] == nums[k - 1]:
                            k -= 1
                        
                        j += 1
                        k -= 1
                    elif target > 0:
                        k -= 1
                    else:
                        j += 1

        return target_list

Solution().threeSum([-1,0,1,2,-1,-4])
