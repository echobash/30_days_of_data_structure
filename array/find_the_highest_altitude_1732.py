from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        altitude = 0
        for change in gain:
            altitude += change
            if altitude > highest_altitude:
                highest_altitude = altitude
        return highest_altitude


sol = Solution()

gain = [-5,1,5,0,-7]
print(f"{gain = } {sol.largestAltitude(gain) = } ")

gain = [-4,-3,-2,-1,4,3,2]
print(f"{gain = } {sol.largestAltitude(gain) = } ")
