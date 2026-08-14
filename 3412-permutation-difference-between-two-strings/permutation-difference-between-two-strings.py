class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        total_difference = 0
        
        for i in range (len(s)):
            char = s[i]

            j = t.index(char)
            
            total_difference += abs(i-j)

        return total_difference
