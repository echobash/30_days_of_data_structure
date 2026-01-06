class Solution:
    def minPartitions(self, n: str) -> int:
        result = 1
        for char in n:
            if int(char) > result:
                result = int(char)
        return result


sol = Solution()

n = "32"
print(f"{n = } | {sol.minPartitions(n) = }")

n = "82734"
print(f"{n = } | {sol.minPartitions(n) = }")

n = "27346209830709182346"
print(f"{n = } | {sol.minPartitions(n) = }")

n = "0"
print(f"{n = } | {sol.minPartitions(n) = }")
