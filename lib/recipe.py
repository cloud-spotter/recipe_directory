class Recipe:
    def __init__(self, id: int, name: str, cooking_time: int, rating: int):
        self.id = id
        self.name = name 
        self.cooking_time = cooking_time
        self.rating = rating

    def __eq__(self, other: object) -> bool:
        return self.__dict__ == other.__dict__
    
    def __repr__(self) -> str:
        return f"Recipe({self.id}, {self.name}, {self.cooking_time}, {self.rating})"