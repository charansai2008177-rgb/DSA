class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        
        for k in range(0, len(nums) - 2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
                
            i = k + 1
            j = len(nums) - 1
            
            while i < j:
                current_sum = nums[i] + nums[j] + nums[k]
                
                if current_sum == 0:
                    result.append([nums[k], nums[i], nums[j]])
                    
                    i += 1
                    j -= 1
                    
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                        
                elif current_sum < 0:
                    i += 1  
                else:
                    j -= 1  
                    
        return result
