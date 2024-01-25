class Solution:
    def containsDuplicate(self, nums) -> bool:
        tmp = set()
        for n in nums:
            if n not in tmp:
                tmp.add(n)
            else:
                return True
        return False

test = [1,1,1,3,3,4,3,2,4,2]

print(Solution().containsDuplicate(test))