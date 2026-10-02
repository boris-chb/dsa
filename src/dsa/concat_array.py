class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        res_arr = [0] * len(nums) * 2
        for i, el in enumerate(nums):
            res_arr[len(nums) + i] = res_arr[i] = el

        return res_arr


if __name__ == "__main__":
    s = Solution()
    r = s.getConcatenation([1, 2, 3, 4, 5])
    print(r)
