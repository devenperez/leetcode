class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        def build(curr: str, na: int, nb: int) -> str:
            if (na == 0 and nb == 0):
                return curr

            if (na == 0 and nb > 2):
                raise "String not possible"

            if (nb == 0 and na > 2):
                raise "String not possible"

            if (len(curr) >= 2 and curr[-1] == curr[-2]):
                if (curr[-1] == 'a'):
                    return build(curr + 'b', na, nb - 1)
                else:
                    return build(curr + 'a', na - 1, nb)
            else:
                if (na > nb):
                    return build(curr + 'a', na - 1, nb)
                else:
                    return build(curr + 'b', na, nb - 1)


        return build("", a, b)