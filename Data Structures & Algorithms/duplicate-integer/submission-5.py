class Solution:
    def hasDuplicate(self, nums):
        hashmap = set()
        for n in nums:
            if n in hashmap:
                return True 
            hashmap.add(n)
        return False