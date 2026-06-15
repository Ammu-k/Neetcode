class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for ind, val in enumerate(nums):
            compliment = target - val
            if compliment in hashmap:
                return [hashmap[compliment], ind]
            hashmap[val] = ind