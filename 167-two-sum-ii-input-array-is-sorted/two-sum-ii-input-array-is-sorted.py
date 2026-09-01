class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        sum=0
        while i != j:
         sum = numbers[i] + numbers[j]
         if sum == target:
             if i>j:
                return [j+1,i+1]
             else:
                return [i+1,j+1]
         elif sum > target:
             j-=1
         else:
             i+=1
        
