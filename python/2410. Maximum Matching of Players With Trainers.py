class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()

        res, i, j = 0, 0, 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                res, i, j = res+1, i+1, j+1
            else:
                j += 1

        return res
