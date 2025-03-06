import arcade
import random
from objetos import Item

SPRITE_SCALING = 0.5
ENEMY_SPRITE = ":resources:images/animated_characters/zombie/zombie_idle.png"


class Enemy(arcade.Sprite):
    def __init__(self, x, y, health=50, attack_power=5):
        super().__init__(ENEMY_SPRITE, SPRITE_SCALING)
        self.center_x = x
        self.center_y = y
        self.health = health
        self.attack_power = attack_power

    def update(self, player):
        pass  # Se puede agregar lógica de movimiento si es necesario

    def take_damage(self, damage):
        """Recibe daño y verifica si muere."""
        self.health -= damage
        if self.health <= 0:
            return self.drop_loot()
        return None

    def attack(self, player):
        """Ataca al jugador."""
        player.health -= self.attack_power
        print(f"El enemigo te atacó e hizo {self.attack_power} de daño!")

    def drop_loot(self):
        """Genera un objeto al morir."""
        loot = Item("Poción", "Recupera vida", 'heal', random.randint(10, 20))
        print("El enemigo dejó caer una poción!")
        return loot
