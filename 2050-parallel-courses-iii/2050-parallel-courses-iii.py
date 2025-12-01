class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        """
        Complexities:
        Time:  O(n^2)
        Space: O(r)

        where n = n, r = len(relations)
        """

        # courses been taken array
        # - O(r) time / O(r) space
        hasPrereq = [False] * n
        prereqMap = [set() for i in range(n)]
        leadsToMap = [set() for i in range(n)]
        for prevCourse, nextCourse in relations:
            hasPrereq[nextCourse - 1] = True
            prereqMap[nextCourse - 1].add(prevCourse)
            leadsToMap[prevCourse - 1].add(nextCourse)

        # O(n) space
        timeUntilComplete = [-1] * n
        coursesCalculated = 0
        maxOverallTimeFound = 0
        toResolve = set()

        # calculate timeUntilComplete for no prereq courses
        # - O(n) time
        for i in range(n):
            if not hasPrereq[i]:
                timeUntilComplete[i] = time[i]
                maxOverallTimeFound = max(maxOverallTimeFound, time[i])
                coursesCalculated += 1
                toResolve.update(leadsToMap[i])

        # find all timeUntilComplete
        # - if all prereq times are known, then calc
        # - O(n^2) time
        while len(toResolve) > 0:
            nextCourse = toResolve.pop()
            maxPrereqTime = -1
            for prereq in prereqMap[nextCourse - 1]:
                if timeUntilComplete[prereq - 1] == -1:
                    maxPrereqTime = -1
                    break
                maxPrereqTime = max(maxPrereqTime, timeUntilComplete[prereq - 1])

            if maxPrereqTime > -1:
                timeUntilComplete[nextCourse - 1] = maxPrereqTime + time[nextCourse - 1]
                maxOverallTimeFound = max(maxOverallTimeFound, timeUntilComplete[nextCourse - 1])
                coursesCalculated += 1
                toResolve.update(leadsToMap[nextCourse - 1])
        


        return maxOverallTimeFound