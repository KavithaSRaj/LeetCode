class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
 
        index = {}
        for k in range(len(nums)):
            index[nums[k]] = k
        for i in range(len(nums)):
            num = target - nums[i]
            if num in index and index[num] != i:
                return [i, index[num]]
                