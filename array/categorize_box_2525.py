class Solution:
    def is_bulky(self, length, width, height):
        volume = length * width * height
        if volume >= 10 ** 9 or length >= 10 ** 4 or width >= 10 ** 4 or height >= 10 ** 4:
            return True
        return False

    def is_heavy(self, mass):
        if mass >= 100:
            return True
        return False

    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        if self.is_bulky(length, width, height) and self.is_heavy(mass):
            return "Both"
        elif not self.is_bulky(length, width, height) and not self.is_heavy(mass):
            return "Neither"
        elif self.is_bulky(length, width, height) and not self.is_heavy(mass):
            return "Bulky"
        elif not self.is_bulky(length, width, height) and self.is_heavy(mass):
            return "Heavy"


sol = Solution()

length = 1000
width = 35
height = 700
mass = 300
print(sol.categorizeBox(length, width, height, mass))

length = 200
width = 50
height = 800
mass = 50
print(sol.categorizeBox(length, width, height, mass))

length = 2
width = 5
height = 8
mass = 5
print(sol.categorizeBox(length, width, height, mass))
