class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # store frequency counts O(n)
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
            

        # find all pairs O(n^2)
        tripleSet = set()

        def addTriple(x,y,z): # O(1) *sort always on 3 items
            triple = [x, y, z]
            triple.sort()
            tripleSet.add(tuple(triple))

        freq_keys = list(frequencies.keys())
        for i in range(len(freq_keys)):
            for j in range(i, len(freq_keys)):
                if i == j and frequencies[freq_keys[i]] < 2:
                    continue

                pair = [freq_keys[i], freq_keys[j]]
                needed = -(pair[0] + pair[1])

                # - check for third in frequency counts O(1)
                if frequencies.get(needed, -1) == -1:
                    # no triple for given pair
                    continue 
                elif needed == pair[0] or needed == pair[1]:
                    if pair[0] == pair[1]:
                        if frequencies[needed] > 2:
                            addTriple(pair[0], pair[1], needed)
                    elif frequencies[needed] > 1:
                        addTriple(pair[0], pair[1], needed)
                else:
                    addTriple(pair[0], pair[1], needed)
                    

        return list(map(lambda tup: list(tup), tripleSet))

        """
        O(n^3) *too slow
        triples = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        t = [nums[i], nums[j], nums[k]]
                        t.sort()
                        triples.add(tuple(t))

        return list(map(lambda tup: list(tup), triples))
        """