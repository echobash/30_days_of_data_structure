class JewelsAndStones:
    def count_gems(self, jewels: str, stones: str) -> int:
        count = 0
        jewels_set = set(jewels)

        for stone in stones:
            if stone in jewels_set:
                count += 1
        return count


jewels = "aA"
stones = "aAAbbbb"
jewels_and_stones = JewelsAndStones()
print(jewels_and_stones.count_gems(jewels, stones))