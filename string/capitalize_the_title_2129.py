from typing import List


class Solution:
    def capitalizeTitle(self, title: str) -> str:
        result = []
        title_list = title.split()
        for word in title_list:
            if len(word) <=2:
                result.append(word.lower())
            else:
                result.append(word.title())
        return " ".join(result)



sol = Solution()

title = "capiTalIze tHe titLe"
print(f"{title = } {sol.capitalizeTitle(title) = }")

title = "First leTTeR of EACH Word"
print(f"{title = } {sol.capitalizeTitle(title) = }")

title = "i lOve leetcode"
print(f"{title = } {sol.capitalizeTitle(title) = }")