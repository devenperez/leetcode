class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Complexities:
        Time:  O(n)
        Space: O(n)

        where n = len(nums)
        """

        # Find j candidates (where nums[i] < nums[j])
        # - j is not 0
        # - nums[j] is not min so far
        # --- O(n)
        jCandidates = []
        minSoFar = nums[0]
        for j in range(1, len(nums)):
            if nums[j] <= minSoFar:
                minSoFar = nums[j]
            else:
                jCandidates.append(j)

        # Fail fast: 0-1 jCandidates = no increasing tuplet (one j candidate will be k)
        if len(jCandidates) <= 1:
            return False

        # Find k candidates (where nums[j] < nums[k])
        # - do the same iteration as j but only over j candidates
        # --- O(n)
        minSoFar = nums[jCandidates[0]]
        for kPrime in range(1, len(jCandidates)):
            if nums[jCandidates[kPrime]] <= minSoFar:
                minSoFar = nums[jCandidates[kPrime]]
            else:
                return True

        return False