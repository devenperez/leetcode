class Solution:
    def findComplement(self, num: int) -> int:
        curr = num
        comp = 0
        pv = 0
        while curr > 0:
            if curr % 2 == 0:
                comp += pow(2,pv)
            
            pv += 1
            curr = curr // 2

        return comp

"""
100
011

4, 1
2, 3
1, 6


101
010

5, 0, 2
2, 1, 1
1, 2


"""