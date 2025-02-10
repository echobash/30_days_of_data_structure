from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruleIndexMapping = {
            "type": 0,
            "color": 1,
            "name": 2
        }

        matching_count = 0
        rows = len(items)

        for i in range(rows):
            if items[i][ruleIndexMapping[ruleKey]] == ruleValue:
                matching_count += 1
        return matching_count


sol = Solution()

items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"

print(f" {items[0]}..... | {ruleKey = } | {ruleValue = } | {sol.countMatches(items,ruleKey,ruleValue) = }")

items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"

print(f" {items[0]}..... | {ruleKey = } | {ruleValue = } | {sol.countMatches(items,ruleKey,ruleValue) = }")
