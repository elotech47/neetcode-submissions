class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            bal = target - n
            if hashmap.get(bal) is not None:
                return [hashmap[bal], i]
            else:
                hashmap[n] = i
        return []

        