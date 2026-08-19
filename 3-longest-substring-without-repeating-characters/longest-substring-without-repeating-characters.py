class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # use right hand to search the letter and add into the net
        # if the letter is seen in the net, left hand need to collect the net back
        # it generate the longers length that is not repeating any letter in the code
        # return the max_len

        #set the net to collect letter
        left = 0
        seen = set()
        max_len = 0

        for right in range (len(s)):
            while s[right]in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            max_len = max(max_len, right-left+1)
        return max_len