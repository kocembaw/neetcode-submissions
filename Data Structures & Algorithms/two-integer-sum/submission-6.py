class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for num, index in enumerate(nums):
            
            needed = target - num

            if needed in seen:
                return [seen[num], seen[needed]]
            seen[num] = index
