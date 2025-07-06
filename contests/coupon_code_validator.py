from typing import List


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        businessLineEnum = {"electronics", "grocery", "pharmacy", "restaurant"}
        n = len(code)
        valid_coupons = {
            "electronics": [],
            "grocery": [],
            "pharmacy": [],
            "restaurant": [],
        }

        for i in range(n):
            if code[i] and (code[i] == '_' or code[i].replace('_', '').isalnum()) and businessLine[
                i] in businessLineEnum and isActive[i]:
                valid_coupons[businessLine[i]].append(code[i])

        result = []

        if len(valid_coupons["electronics"]) > 0:
            result.extend(sorted(valid_coupons["electronics"]))

        if len(valid_coupons["grocery"]) > 0:
            result.extend(sorted(valid_coupons["grocery"]))

        if len(valid_coupons["pharmacy"]) > 0:
            result.extend(sorted(valid_coupons["pharmacy"]))

        if len(valid_coupons["restaurant"]) > 0:
            result.extend(sorted(valid_coupons["restaurant"]))

        return result


sol = Solution()

code = ["SAVE20","","PHARMA5","SAVE@20"]
businessLine = ["restaurant","grocery","pharmacy","restaurant"]
isActive = [True,True,True,True]
print(f"{code = } {businessLine = } {isActive = }  {sol.validateCoupons(code, businessLine, isActive) = }")

code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"]
businessLine = ["grocery","electronics","invalid"]
isActive = [False,True,True]
print(f"{code = } {businessLine = } {isActive = }  {sol.validateCoupons(code, businessLine, isActive) = }")
