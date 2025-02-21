from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        senior_citizens_count = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                senior_citizens_count += 1
        return senior_citizens_count


sol = Solution()

details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
print(f"{details = } {sol.countSeniors(details) = }")

details = ["1313579440F2036","2921522980M5644"]
print(f"{details = } {sol.countSeniors(details) = }")
