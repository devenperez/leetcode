class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        readIndex = 1
        writeIndex = 1

        lastValueSeen = nums[0]
        numTimesValueSeen = 1
        while readIndex < len(nums):
            if nums[readIndex] == lastValueSeen:
                numTimesValueSeen += 1

                if numTimesValueSeen <= 2:
                    nums[writeIndex] = nums[readIndex]
                    writeIndex += 1
            else:
                lastValueSeen = nums[readIndex]
                numTimesValueSeen = 1
                nums[writeIndex] = nums[readIndex]
                writeIndex += 1

            readIndex += 1

        return writeIndex