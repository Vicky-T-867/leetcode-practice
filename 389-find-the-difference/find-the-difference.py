class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        # Calculate the total score of characters in both strings
        # (ord gives each letter a number score)
        sum_s = sum(ord(char) for char in s)
        sum_t = sum(ord(char) for char in t)

        # The difference is the score of the added letter
        extra_code = sum_t - sum_s

        # Convert that score back to a character
        return chr(extra_code)