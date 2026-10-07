# 704. Binary Search
# https://leetcode.com/problems/binary-search/


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            idx = (start + end) // 2
            found = nums[idx]
            if found == target:
                return idx
            elif found < target:
                start = idx + 1
            elif found > target:
                end = idx - 1
        return -1


if __name__ == "__main__":
    s = Solution()
    cases = [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        ([5], 5, 0),
        ([5], 6, -1),
        ([], 1, -1),
        ([2, 5], 2, 0),
    ]

    for nums, target, expected in cases:
        got = s.search(nums, target)
        assert got == expected, (nums, target, got)
