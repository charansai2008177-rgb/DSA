class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        r = 1
        while r<len(nums):
            if len(nums)==1:
                break
            elif nums[l]==0 and nums[r]==0:
                r+=1
            elif nums[l]==0:
                nums[l],nums[r] = nums[r],nums[l]
                r+=1
                l+=1
            else:
                r+=1
                l+=1
                

        