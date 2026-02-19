class MovieRentingSystem:
    def __init__(self, n: int, entries: list[list[int]]):
        self.to_rent = {}
        self.rented = SortedList()
        self.shop_movie_price = {(shop, movie): price for shop, movie, price in entries}

        for shop, movie, price in entries:
            if movie not in self.to_rent:
                self.to_rent[movie] = SortedList()
            self.to_rent[movie].add((price, shop))

    def search(self, movie: int) -> list[int]:
        return [shop for _, shop in self.to_rent.get(movie, [])[:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.shop_movie_price[(shop, movie)]
        self.to_rent[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.shop_movie_price[(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.to_rent[movie].add((price, shop))

    def report(self) -> list[list[int]]:
        return [[shop, movie] for _, shop, movie in self.rented[:5]]

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
