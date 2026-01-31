class Solution(object):
    def reverseString(self, s):
        second = len(s)-1
        first = 0
        while first<len(s)/2:
            temp = s[first]
            s[first] = s[second]
            s[second] = temp
            first = first + 1
            second = second - 1
        
        
