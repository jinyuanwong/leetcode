'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from re import T
from typing import List


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+ nums[j] == target:
#                     return [i,j]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new = sorted(nums)
        min_index = 0
        max_index = len(new)-1
        while max_index> min_index:
            tmp = new[min_index] + new[max_index]
            if tmp == target:
                return [min_index,max_index]
            elif tmp>target:
                max_index-=1
            else:
                min_index+=1


def test():
    nums = [2,7,11,15]
    target = 9
    res = [0, 1]
    solution = Solution()
    if solution.twoSum(nums,target) == res:
        print('The test is passed! ')

test()

