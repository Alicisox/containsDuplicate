class Solution:
    def containsDuplicate(self, nums) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
# Testing
# test = [1,2,3,1]
# test = [1,2,3,4]
test = [1,1,1,3,3,4,3,2,4,2]

print(Solution().containsDuplicate(test))