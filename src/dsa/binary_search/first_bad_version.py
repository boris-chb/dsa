# 278. First Bad Version (Easy)
# https://leetcode.com/problems/first-bad-version/

BAD_VERSION = 1


def isBadVersion(version: int) -> bool:
    return version >= BAD_VERSION


class Solution:
    def firstBadVersion(self, n: int) -> int:
        print(f"\n\n{n=}")
        start, end = 1, n
        best_match = 1  # guaranteed at least one solution
        while start <= end:
            guess = (start + end) // 2
            found = isBadVersion(guess)
            print(f"{best_match=} {start=} {end=} {guess=} ")
            if found:
                best_match = guess
                # try an earlier version
                end = guess - 1
            else:
                # try a later version
                start = guess + 1
        return best_match


if __name__ == "__main__":
    s = Solution()
    cases = [
        (5, 4, 4),
        (1, 1, 1),
        (2, 1, 1),
        (100, 73, 73),
    ]

    for n, bad, expected in cases:
        BAD_VERSION = bad
        got = s.firstBadVersion(n)
        assert got == expected, (n, bad, got)
