class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        max_len = max([len(x) for x in arr])
        sol = [""] * len(arr)
        for l in range(1, max_len + 1):
            seen = {}
            for i, x in enumerate(arr):
                for j in range(len(x) - l + 1):
                    window = x[j:j + l]
                    if seen.get(window) == None or seen.get(window) == i:
                        seen[window] = i
                    else:
                        seen[window] = -1

            # Check if we found everything
            for k in seen.keys():
                if seen[k] == -1:
                    continue
                cur_sol = sol[seen[k]]
                if len(cur_sol) == 0 or (len(k) <= len(cur_sol) and k < cur_sol):
                    sol[seen[k]] = k

            for i in range(len(arr)):
                if len(sol[i]) == 0 and len(arr[i]) > l:
                    break
                if i == len(arr) - 1:
                    return sol

        return sol
