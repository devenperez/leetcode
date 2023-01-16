class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum = sum(nums)
        digitSum = sum(sum(list(map(lambda dStr : int(dStr), str(n)))) for n in nums)
        
        return abs(elementSum - digitSum)