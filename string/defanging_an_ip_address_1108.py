class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


sol = Solution()

address = "1.1.1.1"
print(address, sol.defangIPaddr(address))

address = "255.100.50.0"
print(address, sol.defangIPaddr(address))
