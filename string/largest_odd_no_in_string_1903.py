class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        # Find first odd no from last
        for i in range(n-1,-1,-1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ""


sol = Solution()

num = "52"
print(f"{num=} {sol.largestOddNumber(num)}")

num = "4206"
print(f"{num=} {sol.largestOddNumber(num)}")

num = "35427"
print(f"{num=} {sol.largestOddNumber(num)}")

num = "42062342222222222222221111111111188888000002420040206"
print(f"{num=} {sol.largestOddNumber(num)}")
