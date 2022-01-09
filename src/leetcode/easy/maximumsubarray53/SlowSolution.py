from typing import List


class SlowSolution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Finds largest sum of contiguous subarray within whole array

        :param list nums: Integer array
        :return: Largest sum of a contiguous subarray within whole array
        :rtype: int
        """
        max_sum = self.window_max(nums, 1)
        for window_size in range(2, len(nums)+ 1):
            window_max = self.window_max(nums, window_size)
            if window_max > max_sum:
                max_sum = window_max
        return max_sum

    def window_max(self, nums: List[int], window_size: int) -> int:
        """Finds maximum sum of contiguous subarray within window

        :param list nums: Integer array
        :param int window_size: Length of window
        :return: Largest sum of a contiguous subarray within window
        :rtype: int
        """
        window_max = sum(nums[0:window_size])  # init with first
        for li in range(1, len(nums)):  # left window index (inclusive)
            ri = li + window_size  # right window index (exclusive)
            if ri > len(nums):
                break
            local_max = sum(nums[li:ri])
            if local_max > window_max:  # new max found
                window_max = local_max
        return window_max
