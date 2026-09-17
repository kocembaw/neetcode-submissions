class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()

        for num, index in enumerate(nums):
            seen[num] = index

            needed = target - num

            if needed in seen:
                return [seen[num], seen[needed]]
