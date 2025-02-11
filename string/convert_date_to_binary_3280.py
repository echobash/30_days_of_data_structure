class Solution:
    def decimal_to_binary(self, decimal_no):
        result = ""
        while decimal_no != 0:
            result += str(decimal_no % 2)
            decimal_no = decimal_no // 2
        return result[::-1]

    def convertDateToBinary(self, date: str) -> str:
        year = date.split("-")[0]
        month = date.split("-")[1]
        day = date.split("-")[2]

        year = self.decimal_to_binary(int(year))
        month = self.decimal_to_binary(int(month))
        day = self.decimal_to_binary(int(day))

        return year + "-" + month + "-" + day


sol = Solution()

date = "2080-02-29"
print(f"{date = }  {sol.convertDateToBinary(date) = }")

date = "1900-01-01"
print(f"{date = }  {sol.convertDateToBinary(date) = }")
