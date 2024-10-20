class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height)
        right = [0] * len(height)

        waterGathered = 0
        for i in range(len(height)):
            if i > 0:
                left[i] = max(left[i-1], height[i-1])

            backI = len(height) - i - 1
            if backI < len(height) - 1:
                right[backI] = max(right[backI + 1], height[backI + 1])
        
        for i in range(len(height)):
            waterGathered += max(0, min(left[i], right[i]) - height[i])

        return waterGathered