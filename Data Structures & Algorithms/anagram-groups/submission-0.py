class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for st in strs:
            sortedS = ''.join(sorted(st))
            hashmap[sortedS].append(st)
        return list(hashmap.values())

        