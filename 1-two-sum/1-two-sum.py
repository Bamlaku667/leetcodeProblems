class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        sum = target
        listOfIndex = []
        for i in range (len(nums)):
            diff = sum - nums[i]
            if diff  not in hashTable:
                hashTable[nums[i]] = nums[i]
            else:
                listOfIndex.append(nums.index(diff))
                listOfIndex.append(i)
                
                hashTable[nums[i]] = nums[i]
        return listOfIndex
    
    
        
        
    