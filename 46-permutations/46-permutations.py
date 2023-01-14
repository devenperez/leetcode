class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permute_with_prefix(nums: List[int], prefix: List[int]):
            # Base case
            if len(nums) == 1:
                return [prefix + nums]
            
            permutations = []
            for i in range(len(nums)):
                 permutations.extend(permute_with_prefix(nums[:i] + nums[(i + 1):], # Remove the ith element from nums
                                                         prefix + [nums[i]]))
            return permutations
        
        # Initial call
        return permute_with_prefix(nums, [])