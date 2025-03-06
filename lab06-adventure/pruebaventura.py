import arcade
import random
from mapas import MapManager
from personaje import Player
from enemigos import Enemy
from interfaz import GameInterface
from objetos import Item

# Configuración básica
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Juego de Aventuras"


class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.AMAZON)

        self.map_manager = MapManager()
        self.player = Player()
        self.enemies = []
        self.items = []
        self.interface = None

        self.setup()

    def setup(self):
        """Inicializa el juego"""
        self.map_manager.load_map()
        self.enemies = [Enemy(x, y) for x, y in self.map_manager.spawn_enemies()]
        self.items = [Item("Poción Curativa", "Recupera vida", 'heal', random.randint(20, 50)) for _ in range(2)]

        from interfaz import GameInterface
        self.interface = GameInterface(self)

    def on_draw(self):
        arcade.start_render()
        self.map_manager.draw()
        self.player.draw()
        for enemy in self.enemies:
            enemy.draw()
        for item in self.items:
            item.draw()
        if self.interface:
            self.interface.draw()

    def on_update(self, delta_time):
        self.player.update()
        for enemy in self.enemies:
            enemy.update(self.player)

    def on_key_press(self, key, modifiers):
        self.player.handle_input(key, modifiers, self.enemies, self.items)

        if key == arcade.key.ENTER:
            for enemy in self.enemies:
                if abs(enemy.x - self.player.x) < 50 and abs(enemy.y - self.player.y) < 50:
                    self.interface.show_combat_menu(enemy)
                    if enemy.health <= 0:
                        self.enemies.remove(enemy)
                    break


if __name__ == "__main__":
    game = GameWindow()
    arcade.run()
