class Solution(object):
    def firstUniqChar(self, s):
        for i, ch in enumerate(s):
            if s.index(ch) == s.rindex(ch):
                return i
        return -1
