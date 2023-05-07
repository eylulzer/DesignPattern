from typing import List, Optional


class MenuItem:
    def __init__(self, name: str, description: str, price: float, meal_type: str, is_vegan: bool, is_vegetarian: bool):
        self.name = name
        self.description = description
        self.price = price
        self.meal_type = meal_type
        self.is_vegan = is_vegan
        self.is_vegetarian = is_vegetarian

    def __str__(self):
        return f"{self.name} - {self.description} - ${self.price} - {self.meal_type}"


class Menu:
    def __init__(self):
        self.menu_items = []

    def add_item(self, item: MenuItem):
        self.menu_items.append(item)

    def get_items_by_type(self, meal_type: str) -> List[MenuItem]:
        return [item for item in self.menu_items if item.meal_type == meal_type]

    def get_vegan_items(self) -> List[MenuItem]:
        return [item for item in self.menu_items if item.is_vegan]

    def get_vegetarian_items(self) -> List[MenuItem]:
        return [item for item in self.menu_items if item.is_vegetarian]


class MenuIterator:
    def has_next(self) -> bool:
        raise NotImplementedError()

    def next(self) -> Optional[MenuItem]:
        raise NotImplementedError()


class MealTypeIterator(MenuIterator):
    def __init__(self, items: List[MenuItem], meal_type: str):
        self.items = items
        self.current_index = 0
        self.meal_type = meal_type

    def has_next(self) -> bool:
        while self.current_index < len(self.items):
            if self.items[self.current_index].meal_type == self.meal_type:
                return True
            self.current_index += 1
        return False

    def next(self) -> Optional[MenuItem]:
        if self.has_next():
            item = self.items[self.current_index]
            self.current_index += 1
            return item
        return None


class DietaryIterator(MenuIterator):
    def __init__(self, items: List[MenuItem], dietary_type: str):
        self.items = items
        self.current_index = 0
        self.dietary_type = dietary_type

    def has_next(self) -> bool:
        while self.current_index < len(self.items):
            if (self.dietary_type == "vegan" and self.items[self.current_index].is_vegan) or \
                    (self.dietary_type == "vegetarian" and self.items[self.current_index].is_vegetarian):
                return True
            self.current_index += 1
        return False

    def next(self) -> Optional[MenuItem]:
        if self.has_next():
            item = self.items[self.current_index]
            self.current_index += 1
            return item
        return None

menu = Menu()

menu.add_item(MenuItem("Sezar Salatası", "Marul ve parmesan", 12.0, "aperatif", False, True))
menu.add_item(MenuItem("Veggie Burger", "Sebzeli burger", 10.0, "ana_yemek", False, True))
menu.add_item(MenuItem("Vegan Köfte", "Mercimek köftesi", 8.0, "ana_yemek", True, True))
menu.add_item(MenuItem("Çikolatalı Soufflé", "Sıcak çikolatalı soufflé", 7.0, "tatlı", False, True))
menu.add_item(MenuItem("Meyve Salatası", "Taze meyve karışımı", 5.0, "tatlı", True, True))

# İterator'ları kullanarak menü öğelerinin listelenmesi
meal_type_iterator = MealTypeIterator(menu.menu_items, "tatlı")
while meal_type_iterator.has_next():
    print(meal_type_iterator.next())

print("------")

vegan_iterator = DietaryIterator(menu.menu_items, "vegan")
while vegan_iterator.has_next():
    print(vegan_iterator.next())

print("------")

vegetarian_iterator = DietaryIterator(menu.menu_items, "vegetarian")
while vegetarian_iterator.has_next():
    print(vegetarian_iterator.next())

