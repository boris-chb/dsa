class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # {num: idx}

        for i, num in enumerate(nums):
            pair = target - num
            if pair in seen:
                return [seen[pair], i]
            seen[num] = i

        raise ValueError("no solution")


if __name__ == "__main__":
    s = Solution()
    ans1 = s.twoSum([1, 2, 3, 4, 5], 8)
