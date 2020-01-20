class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        h = collections.Counter(-a - b for a in A for b in B)
        return sum(h[c + d] for c in C for d in D)
