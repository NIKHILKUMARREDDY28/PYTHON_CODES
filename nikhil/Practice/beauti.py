def f(s,i):
    l,r = i,i
    len1 = 0
    while l >= 0 and r <len(s)  and s[l] == s[r]:
        len1 = max(len1,r-l+1)
        l -= 1
        r += 1
    return len1
class Solution:
    def solve(self,A,B):
        lis = []
        for i in B:
            lis.append(f(A,i-1))
        return lis
sol = Solution()