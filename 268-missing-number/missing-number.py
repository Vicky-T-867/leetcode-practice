class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #arrage the order
        nums.sort()
        #Check the number match the position
        for i in range (len(nums)):
            if nums[i] !=i:
                return i
        return len(nums)


