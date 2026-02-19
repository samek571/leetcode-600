class Solution:
    def countCollisions(self, directions: str) -> int:
        data = directions.lstrip("L").rstrip("R")
        return len(data) - data.count("S")
