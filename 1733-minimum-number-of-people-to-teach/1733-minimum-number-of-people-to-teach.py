class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        
        uniquePplInOddFriendships = set()
        langsInOddFriendships = [0] * n
        for _p1, _p2 in friendships:
            p1 = _p1 - 1
            p2 = _p2 - 1

            langs = set(languages[p1] + languages[p2])

            if len(langs) == len(languages[p1]) + len(languages[p2]):
                if _p1 not in uniquePplInOddFriendships:
                    uniquePplInOddFriendships.add(_p1)
                    for l in languages[p1]:
                        langsInOddFriendships[l - 1] += 1

                if _p2 not in uniquePplInOddFriendships:
                    uniquePplInOddFriendships.add(_p2)
                    for l in languages[p2]:
                        langsInOddFriendships[l - 1] += 1
                

        enumerated = list(enumerate(langsInOddFriendships))
        enumerated.sort(key=lambda x : x[1])
        maxKnownLang, numKnownBy = enumerated[-1]

        return len(uniquePplInOddFriendships) - numKnownBy

