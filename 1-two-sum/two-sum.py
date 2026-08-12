class Solution:
    #example
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            target_value = target - num
            if target_value in seen:
                return [seen[target_value],i]
            seen[num] = i
        