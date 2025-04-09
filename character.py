class Character():
    def __init__(self, name, max_health, strong, armor):
        self.name = name
        self.health = max_health
        self.strong = strong
        self.armor = armor
        self.current_health = 100

    def attack(self, target):
        target.current_health -= self.strong * ((100 - target.armor) / 100)
    
    def get_current_state(self):
        state = (f"Имя: {self.name}\n"
        f"Здоровье: {self.current_health}/{self.health}\n"
        f"Броня: {self.armor}%\n"
        f"Атака: {self.strong}")
        return state


class Enemy(Character):
    def __init__(self, name, max_health, strong, armor):
        super().__init__(name, max_health, strong, armor)


class Player(Character):
    def __init__(self, name, max_health, strong, armor):
        super().__init__(name, max_health, strong, armor)
        self.inventory = Inventory(32)


class Inventory():
    def __init__(self, size):
        self.items = []
        self.max_size = size
    
    def add_item(self, item):
        if len(self.items) < self.max_size:
            self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items
    
    def __str__(self):
        return str(self.items)


class Item():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return self.name

# Тестируем наши объекты
main_character = Player("Игрок", 15, 5, 0)
goblin = Enemy("Гоблин", 100, 2, 20)

main_character.attack(goblin)
goblin.attack(main_character)

print(main_character.get_current_state())
print(goblin.get_current_state())

item = Item("Супер Предмет")

main_character.inventory.add_item(item)

print(main_character.inventory.get_items())