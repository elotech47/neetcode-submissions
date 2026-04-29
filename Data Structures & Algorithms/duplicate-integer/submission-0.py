class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_seens = []
        for n in nums:
            if n in num_seens:
                return True
            else:
                num_seens.append(n)
        return False

        