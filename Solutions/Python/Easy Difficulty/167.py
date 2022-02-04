'''167. Two Sum II - Input Array Is Sorted'''


class Solution:
    def twoSum(self, nums, target):
        '''First Solution'''

        dic = {}
        for index, num in enumerate(nums):
            if target-num in dic:
                return [dic[target-num]+1, index+1]
            dic[num] = index

        '''Second Solution'''

        pointer_left = 0
        pointer_right = len(nums)-1

        while pointer_left < pointer_right:
            current_sum = nums[pointer_left] + nums[pointer_right]

            if current_sum == target:
                return [pointer_left+1, pointer_right+1]

            if current_sum < target:
                pointer_left += 1

            else:
                pointer_right -= 1


s = Solution()
print(s.twoSum([2, 3, 4], 6))
print(s.twoSum([-1, 0], -1))
print(s.twoSum([2, 7, 11, 15], 9))
