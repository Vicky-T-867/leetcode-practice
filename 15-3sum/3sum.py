class Solution(object):

    def threeSum(self, nums):
        # 1. ALWAYS SORT FIRST
        nums.sort()  # [-4, -1, -1, 0, 1, 2]
        result = []

        # 2. Main loop for fixed number
        for i in range(len(nums)):

            # Skip duplicate fixed numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            start = i + 1
            end = len(nums) - 1

            while start < end:
                total = nums[i] + nums[start] + nums[end]

                if total > 0:
                    end -= 1
                elif total < 0:
                    start += 1
                else:
                    # Found a triplet!
                    result.append([nums[i], nums[start], nums[end]])

                    start += 1
                    end -= 1

                    # Skip duplicate numbers on the start position
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1

        # 3. MUST BE OUTSIDE ALL LOOPS (at the far left)
        return result