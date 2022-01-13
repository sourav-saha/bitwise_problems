'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

Leetcode: https://leetcode.com/problems/subsets-ii/
'''

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        
        for i in range((1<<n)):
            sublist = []
            for bitPos in range(n):
                if (i&(1<<bitPos)):
                    sublist.append(nums[bitPos])
            res.append(sorted(sublist))  #important to append the sorted sublist otherwise following sort won't work
        
        # finally, sort the res list as it will have duplicates
        new_res = []
        for elem in res:
            if elem not in new_res:
                new_res.append(elem)
        
        return new_res
