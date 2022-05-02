class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort(key=lambda x: x[0])
        
        # Go throught the things and merge
        newIntervals = [intervals[0]]
        for i in range(len(intervals) - 1):
            lastIndex = len(newIntervals) - 1
            
            start = newIntervals[lastIndex][0]
            end = newIntervals[lastIndex][1]
            nextStart = intervals[i + 1][0]
            nextEnd = intervals[i + 1][1]
            
            smallestStart = min(start, nextStart)
            biggestEnd = max(end, nextEnd)
            
            if end >= nextStart:
                newIntervals[lastIndex] = [smallestStart, biggestEnd]
            else:
                newIntervals.append(intervals[i + 1])
        return newIntervals