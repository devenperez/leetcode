class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        new = [0] * forget
        new[0] = 1
        total_known = 1
        cant_tell = 1

        for i in range(1, n):
            index = i % forget
            forget_index = index
            delay_index = (i - delay + forget) % forget

            total_known -= new[forget_index]
            cant_tell -= new[delay_index]

            new[index] = total_known - cant_tell
            cant_tell += new[index]
            total_known += new[index]

        return total_known % (10 ** 9 + 7)