import random
from abc import ABC, abstractmethod


# region Weapons
class Weapon(ABC):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def __init__(self):
        super().__init__("Меч", 15)

    def attack(self):
        return self.damage


# Копьё
class Spear(Weapon):
    def __init__(self):
        super().__init__("Копье", 20)

    def attack(self):
        return self.damage * 1.2  # Бонус для копья


class Bow(Weapon):
    def __init__(self):
        super().__init__("Лук", 12)

    def attack(self):
        return self.damage * 1.5  # Бонус для лука
# endregion


# region Characters
class Character(ABC):
    def __init__(self, name, level, health, weapon=None, special_ability=None):
        self.name = name
        self.level = level
        self.health = health
        self.weapon = weapon
        self.special_ability = special_ability

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self, damage):
        pass

    @abstractmethod
    def use_special_ability(self):
        pass

    def is_alive(self):
        return self.health > 0

    def __del__(self):
        print(f"{self.name} удалён!\n")
        print(f"{self.name} покидает поле боя...")


class Swordsman(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 100 + level * 10, Sword(), "Мощный удар")

    def attack(self):
        damage = self.weapon.attack() * (1 + 0.1 * self.level)
        print(f"{self.name} атакует мечом и наносит {damage:.1f} урона!")
        return damage

    def defend(self, damage):
        reduced_damage = damage * 0.7  # Мечник хорошо блокирует
        self.health -= reduced_damage
        print(
            f"{self.name} блокирует атаку и получает {reduced_damage:.1f} урона. "
            f"Осталось здоровья: {self.health:.1f}")

    def use_special_ability(self):
        damage = self.weapon.attack() * 2 * (1 + 0.1 * self.level)
        print(f"{self.name} использует {self.special_ability} и наносит {damage:.1f} урона!")
        return damage


class Rider(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 120 + level * 8, Spear(), "Атака с разгона")

    def attack(self):
        damage = self.weapon.attack() * (1 + 0.08 * self.level)
        print(f"{self.name} атакует копьем и наносит {damage:.1f} урона!")
        return damage

    def defend(self, damage):
        reduced_damage = damage * 0.8  # Всадник хуже блокирует
        self.health -= reduced_damage
        print(f"{self.name} получает {reduced_damage:.1f} урона. Осталось здоровья: {self.health:.1f}")

    def use_special_ability(self):
        damage = self.weapon.attack() * 1.8 * (1 + 0.08 * self.level)
        print(f"{self.name} использует {self.special_ability} и наносит {damage:.1f} урона!")
        return damage


class Archer(Character):
    def __init__(self, name, level):
        super().__init__(name, level, 80 + level * 12, Bow(), "Меткий выстрел")

    def attack(self):
        damage = self.weapon.attack() * (1 + 0.12 * self.level)
        print(f"{self.name} стреляет из лука и наносит {damage:.1f} урона!")
        return damage

    def defend(self, damage):
        self.health -= damage  # Лучник плохо блокирует
        print(f"{self.name} получает {damage:.1f} урона. Осталось здоровья: {self.health:.1f}")

    def use_special_ability(self):
        damage = self.weapon.attack() * 2.5 * (1 + 0.12 * self.level)
        print(f"{self.name} использует {self.special_ability} и наносит {damage:.1f} урона!")
        return damage
# endregion


# region Monsters
class Monster(ABC):
    def __init__(self, level, health, special_ability):
        self.level = level
        self.health = health
        self.special_ability = special_ability

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def evade(self):
        pass

    @abstractmethod
    def use_special_ability(self):
        pass

    def is_alive(self):
        return self.health > 0

    def __del__(self):
        print(f"Монстр {self.__class__.__name__} удалён!")


class Spider(Monster):
    def __init__(self, level):
        super().__init__(level, 50 + level * 5, "Ядовитый укус")

    def attack(self):
        damage = 8 + self.level * 2
        print(f"Паук атакует и наносит {damage} урона!")
        return damage

    def evade(self):
        return random.random() < 0.3  # 30% шанс увернуться

    def use_special_ability(self):
        damage = 15 + self.level * 3
        print(f"Паук использует {self.special_ability} и наносит {damage} урона!")
        return damage


class WingedBeast(Monster):
    def __init__(self, level):
        super().__init__(level, 60 + level * 6, "Устрашающий крик")

    def attack(self):
        damage = 10 + self.level * 2
        print(f"Крылатая тварь атакует и наносит {damage} урона!")
        return damage

    def evade(self):
        return random.random() < 0.4  # 40% шанс увернуться

    def use_special_ability(self):
        print(f"Крылатая тварь использует {self.special_ability} и оглушает противника!")
        return 0  # Спецспособность не наносит урон, но может иметь другие эффекты


class Werewolf(Monster):
    def __init__(self, level):
        super().__init__(level, 70 + level * 7, "Свирепый укус")

    def attack(self):
        damage = 12 + self.level * 2
        print(f"Волколак атакует и наносит {damage} урона!")
        return damage

    def evade(self):
        return random.random() < 0.25  # 25% шанс увернуться

    def use_special_ability(self):
        damage = 20 + self.level * 3
        print(f"Волколак использует {self.special_ability} и наносит {damage} урона!")
        return damage


class UnderwaterMonster(Monster):
    def __init__(self, level):
        super().__init__(level, 80 + level * 5, "Удар щупальцем")

    def attack(self):
        damage = 15 + self.level * 2
        print(f"Подводный монстр атакует и наносит {damage} урона!")
        return damage

    def evade(self):
        return random.random() < 0.2  # 20% шанс увернуться

    def use_special_ability(self):
        damage = 25 + self.level * 3
        print(f"Подводный монстр использует {self.special_ability} и наносит {damage} урона!")
        return damage


class Dragon(Monster):
    def __init__(self, level):
        super().__init__(level, 100 + level * 10, "Испепеление")

    def attack(self):
        damage = 20 + self.level * 3
        print(f"Дракон атакует и наносит {damage} урона!")
        return damage

    def evade(self):
        return random.random() < 0.1  # 10% шанс увернуться

    def use_special_ability(self):
        damage = 40 + self.level * 5
        print(f"Дракон использует {self.special_ability} и наносит {damage} урона!")
        return damage
# endregion


# region Game process
def create_random_monster(level):
    monster_classes = [Spider, WingedBeast, Werewolf, UnderwaterMonster, Dragon]
    monster_class = random.choice(monster_classes)
    return monster_class(level)


# Основная логика игры
def game():
    print("Выберите персонажа:")
    print("1. Мечник")
    print("2. Всадник")
    print("3. Лучник")

    choice = input("Ваш выбор (1-3): ")
    name = input("Введите имя персонажа: ")
    level = int(input("Введите уровень персонажа (1-10): "))

    if choice == "1":
        hero = Swordsman(name, level)
    elif choice == "2":
        hero = Rider(name, level)
    elif choice == "3":
        hero = Archer(name, level)
    else:
        print("Неверный выбор. По умолчанию создан Мечник.")
        hero = Swordsman(name, level)

    print(f"\nСоздан персонаж: {hero.name}, уровень {hero.level}, здоровье {hero.health}")
    print(f"Вооружение: {hero.weapon.name}, специальная способность: {hero.special_ability}")

    # Генерация монстров
    numOfMonsters = random.randint(2, 5)
    currMonsters = [create_random_monster(random.randint(1, level + 2)) for _ in range(numOfMonsters)]
    print(f"\nВпереди {numOfMonsters} монстров! Приготовьтесь к бою!\n")

    for i, monster in enumerate(currMonsters, 1):
        print(f"\n=== Бой {i} ===")
        print(f"Противник: {monster.__class__.__name__}, уровень {monster.level}, здоровье {monster.health}")

        # Бой с текущим противником
        while hero.is_alive() and monster.is_alive():
            # Ход героя
            print("\nВаш ход:")
            action = input("Выберите действие (1 - атака, 2 - спецспособность): ")

            if action == "1":
                currDamage = hero.attack()
            elif action == "2":
                currDamage = hero.use_special_ability()
            else:
                print("Неверный выбор. Автоматически выбрана атака.")
                currDamage = hero.attack()

            # Проверка, увернулся ли монстр
            if monster.evade():
                print(f"{monster.__class__.__name__} увернулся от атаки!")
            else:
                monster.health -= currDamage

            # Монстр умер после атаки
            if not monster.is_alive():
                print(f"\n{monster.__class__.__name__} повержен!")
                break

            # Ход монстра
            print("\nХод монстра:")
            if random.random() < 0.3:  # 30% шанс использовать спецспособность
                currDamage = monster.use_special_ability()
            else:
                currDamage = monster.attack()

            hero.defend(currDamage)

        if not hero.is_alive():
            print("\nВы проиграли! Ваш персонаж погиб.")
            break


    if hero.is_alive():
        print("\nПоздравляем! Вы победили всех монстров!")
# endregion


# Запуск игры
if __name__ == "__main__":
    game()