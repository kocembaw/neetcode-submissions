class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            
            needed = target - num

            if needed in seen:
                temp = [seen[num], seen[needed]]
                return temp
            seen[num] = index
