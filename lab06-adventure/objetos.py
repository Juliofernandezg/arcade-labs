import arcade
import random

SPRITE_SCALING = 0.5
ITEM_SPRITE = ":resources:images/items/gemBlue.png"


class Item(arcade.Sprite):
    def __init__(self, name, description, effect, value, x=0, y=0):
        super().__init__(ITEM_SPRITE, SPRITE_SCALING)
        self.name = name
        self.description = description
        self.effect = effect  # 'heal', 'boost', 'shield', 'dot', 'revive'
        self.value = value
        self.center_x = x
        self.center_y = y

    def get_damage_multiplier(self):
        """Devuelve el multiplicador de daño si es un objeto de ataque."""
        return self.value if self.effect == 'boost' else 1

    def use(self, player):
        """Aplica el efecto del objeto al jugador."""
        if self.effect == 'heal':
            player.health += self.value
            print(f"{player.health} HP restaurados!")
        elif self.effect == 'boost':
            player.attack_power *= self.value
            print(f"Ataque aumentado a {player.attack_power}!")
        elif self.effect == 'shield':
            player.shield = self.value
            print(f"Escudo activado con {self.value} de resistencia!")
        elif self.effect == 'dot':
            player.apply_dot(self.value)
            print("Efecto de daño por turno activado!")
        elif self.effect == 'revive':
            if player.health <= 0:
                player.health = self.value
                print(f"Reviviste con {self.value} HP!")


# Generación de objetos innovadores

ITEMS = [
    Item("Poción Curativa", "Recupera vida", 'heal', random.randint(20, 50)),
    Item("Fuerza Bruta", "Duplica el ataque por 3 turnos", 'boost', 2),
    Item("Escudo Energético", "Absorbe daño durante 5 turnos", 'shield', 50),
    Item("Veneno Persistente", "Inflige daño continuo al enemigo", 'dot', 5),
    Item("Resurrección", "Revive al jugador con la mitad de la vida", 'revive', 50),
]