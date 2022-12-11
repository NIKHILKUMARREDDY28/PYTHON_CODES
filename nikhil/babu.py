class Solution(object):
    def groupAnagrams(self, strs):
        mys = ["".join(sorted(i)) for i in strs]
        return mys


obj=Solution()
a=[x for x in input().split()]
print(obj.groupAnagrams(a))