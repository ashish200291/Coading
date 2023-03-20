class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in mapper:
                return [mapper[diff],i]
            mapper[n] = i
        return []
