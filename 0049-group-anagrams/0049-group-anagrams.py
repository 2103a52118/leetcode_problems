class Solution:
    def groupAnagrams(self, a: List[str]) -> List[List[str]]:
        return reduce(lambda d,s:d[tuple(sorted(s))].append(s) or d,a,defaultdict(list)).values()