import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        
        # Heapify (min) the first k elements
        heapq.heapify(heap)

        # iterate over k+1...n - O(n) times
        #  - if larger than min in heap, replace min - O(log k)
        #  - else do nothing
        for i in range(k, len(nums)):
            num = nums[i]
            if num > heap[0]:
                heapq.heapreplace(heap, num)

        # return min in heap
        return heap[0]