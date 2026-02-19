class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_set = {}
        self.pq = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_set[food] = (cuisine, rating)
            if cuisine not in self.pq:
                self.pq[cuisine] = []
            heapq.heappush(self.pq[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food_set[food]
        self.food_set[food] = (cuisine, newRating)
        heapq.heappush(self.pq[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.pq[cuisine]
        while heap:
            rating_neg, food = heap[0]
            if self.food_set[food][1] == -rating_neg:
                return food
            heapq.heappop(heap)
        return ""


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
