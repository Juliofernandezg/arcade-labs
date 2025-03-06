import arcade

SPRITE_SCALING = 0.5
PLAYER_SPRITE = ":resources:images/animated_characters/female_person/femalePerson_idle.png"


class Player(arcade.Sprite):
    def __init__(self):
        super().__init__(PLAYER_SPRITE, SPRITE_SCALING)
        self.center_x = 400
        self.center_y = 300
        self.health = 100
        self.attack_power = 10
        self.inventory = []  # Lista de objetos en el inventario
        self.equipped_item = None  # Objeto equipado

    def update(self):
        pass  # Implementar lógica de movimiento si es necesario

    def handle_input(self, key, modifiers, enemies, items):
        if key == arcade.key.SPACE:
            self.attack(enemies)
        elif key == arcade.key.E:
            self.pick_up_item(items)
        elif key == arcade.key.I:
            self.show_inventory()

    def attack(self, enemies):
        """Ataca al enemigo más cercano."""
        if enemies:
            enemy = enemies[0]  # Placeholder, mejorar con detección de proximidad
            damage = self.attack_power
            if self.equipped_item:
                damage *= self.equipped_item.get_damage_multiplier()
            enemy.take_damage(damage)
            print(f"Atacaste al enemigo y le hiciste {damage} de daño!")

    def pick_up_item(self, items):
        """Recoge un objeto cercano y lo agrega al inventario."""
        if items:
            item = items.pop(0)  # Placeholder, mejorar con detección de proximidad
            self.inventory.append(item)
            print(f"Recogiste {item.name}!")

    def use_item(self, item):
        """Usa un objeto del inventario."""
        if item in self.inventory:
            if item.effect == 'heal':
                self.health += item.value
                print(f"Restauraste {item.value} puntos de vida!")
            elif item.effect == 'boost':
                self.attack_power *= item.value
                print(f"Tu ataque ahora es {self.attack_power}!")
            self.inventory.remove(item)

    def show_inventory(self):
        """Muestra el inventario y estadísticas."""
        print("Inventario:")
        for item in self.inventory:
            print(f"- {item.name}: {item.description}")
        print(f"Vida: {self.health}")
        print(f"Ataque: {self.attack_power}")
