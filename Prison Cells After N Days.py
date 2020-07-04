class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        L = len(cells)
        def nextday(c: List[int]) -> List[int]:
            res = [0]*L
            for i in range(1, L-1):
                res[i] = int(not(c[i-1] != c[i+1]))
            return res
        if N % 14 == 0: N = 14
        else: N = N % 14
        for i in range(N):
            cells = nextday(cells)
        return cells