from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    s = Solution()
    r1 = s.isAnagram("racecar", "carrace")
    r2 = s.isAnagram("jam", "jar")
    print(f"{r1=}")
    print(f"{r2=}")
