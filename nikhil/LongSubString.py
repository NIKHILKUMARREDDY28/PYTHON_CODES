class Solution:
    def fun(self, n):
        l = [x for x in n]
        s = set(l)
        if (len(l) == len(s)):
            return len(s)
        else:
            return -1

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(n) - 1):
            for j in range(i + 1, len(n)):
                curr_len = self.fun(n[i:j])
                if max_len < curr_len:
                    max_len = curr_len
                if (curr_len == -1):
                    break
        return max_len
n = input()
obj = Solution()
print(obj.lengthOfLongestSubstring(n))