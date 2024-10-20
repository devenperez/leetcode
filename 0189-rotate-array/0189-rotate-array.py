class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)

        buffer = nums[-k:]
        buffI = 0
        for i in range(len(nums)):
            tmp = nums[i]
            nums[i] = buffer[buffI]
            buffer[buffI] = tmp
            buffI = (buffI + 1) % len(buffer)


        # O(kn) time / O(1) space -- too slow
        # for _ in range(k):
        #     lastNum = nums[-1]
        #     for i in range(len(nums)):
        #         tmp = nums[i]
        #         nums[i] = lastNum
        #         lastNum = tmp
