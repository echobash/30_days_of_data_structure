class JewelsAndStones:
    def count_gems(self, jewels: str, stones: str) -> int:
        jewel_count = 0

        for stone in stones:
            if stone in jewels:
                jewel_count += 1
        return jewel_count


jewels = "aA"
stones = "aAAbbbb"
jewels_and_stones = JewelsAndStones()
print(jewels_and_stones.count_gems(jewels, stones))