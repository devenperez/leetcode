class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(len(nums)):
            if i > 0:
                left[i] = left[i - 1] * nums[i - 1]
            
            if n - i < len(nums):
                right[n - i - 1] = right[n - i] * nums[n - i]

        return [left[i] * right[i] for i in range(len(nums))]