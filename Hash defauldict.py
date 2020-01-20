import collections
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        a=collections.defaultdict(list)
        for i in strs:
            a[tuple(sorted(i))].append(i)#因为list不能hash，所以使用tuple作为key
        return a.values()