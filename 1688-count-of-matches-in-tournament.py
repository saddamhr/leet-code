class Solution:
    def numberOfMatches(self, n: int) -> int:
        total_matches = 0
        while n > 1:
            matches_played_in_round = n // 2
            total_matches += matches_played_in_round
            n = n - matches_played_in_round
        return total_matches

print(Solution().numberOfMatches(7))