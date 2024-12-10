from collections import defaultdict
class JewelsAndStones:
    def count_gems(self, jewels: str, stones: str) -> int:
        jewel_count = defaultdict(int)
        count = 0
        for jewel in jewels:
            jewel_count[jewel] += 1

        for stone in stones:
            if stone in jewel_count:
                count += 1
        return count


jewels = "aA"
stones = "aAAbbbb"
jewels_and_stones = JewelsAndStones()
print(jewels_and_stones.count_gems(jewels, stones))