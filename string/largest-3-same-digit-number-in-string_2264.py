class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        max_no = -1
        if n == 3 and (num[0] == num[1] == num[2]):
            return num

        for i in range(n-2):
            if num[i] == num[i+1] == num[i+2]:
                max_no = max(int(max_no), int(num[i]))
        return str(max_no) * 3 if max_no != -1 else ""


sol = Solution()

num = "6777133339"
print(f"{num = } {sol.largestGoodInteger(num) = }")

num = "2300019"
print(f"{num = } {sol.largestGoodInteger(num) = }")

num = "42352338"
print(f"{num = } {sol.largestGoodInteger(num) = }")

num = "123"
print(f"{num = } {sol.largestGoodInteger(num) = }")

num = "444"
print(f"{num = } {sol.largestGoodInteger(num) = }")

num = "1221000"
print(f"{num = } {sol.largestGoodInteger(num) = }")
