class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        noDupes = set(nums)
        return len(noDupes) != len(nums)


if __name__ == "__main__":
    s = Solution()
    r1 = s.hasDuplicate([1, 2, 2, 3, 3])
    r2 = s.hasDuplicate([1, 2, 3])
    print(f"{r1=}")
    print(f"{r2=}")
