class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            
        arry = []
        for num, cnt in count.items():
            arry.append([cnt, num])
        arry.sort()

        result = []
        while len(result) < k:
            result.append(arry.pop()[1])
        return result
