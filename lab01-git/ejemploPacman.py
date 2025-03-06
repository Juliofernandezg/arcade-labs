import arcade
import os

# Constantes del juego
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pac-Man"

# Ruta de los sprites
SPRITE_PATH = "/mnt/data/pacman-art/pacman-art"


class PacManGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        self.player_sprite = None
        self.wall_list = None
        self.dot_list = None
        self.ghost_list = None
        self.physics_engine = None

    def setup(self):
        """ Configura los elementos del juego """
        self.player_sprite = arcade.Sprite(os.path.join(SPRITE_PATH, "pacman-down/1.png"), 0.5)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50

        self.wall_list = arcade.SpriteList()
        self.dot_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()

        # Añadir puntos
        dot = arcade.Sprite(os.path.join(SPRITE_PATH, "other/dot.png"), 0.5)
        dot.center_x = 200
        dot.center_y = 200
        self.dot_list.append(dot)

        # Añadir fantasmas
        blinky = arcade.Sprite(os.path.join(SPRITE_PATH, "ghosts/blinky.png"), 0.5)
        blinky.center_x = 400
        blinky.center_y = 300
        self.ghost_list.append(blinky)

        # Añadir paredes (ejemplo)
        wall = arcade.Sprite(os.path.join(SPRITE_PATH, "other/apple.png"), 0.5)
        wall.center_x = 100
        wall.center_y = 100
        self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        """ Dibuja todos los elementos en la pantalla """
        arcade.start_render()
        self.wall_list.draw()
        self.dot_list.draw()
        self.ghost_list.draw()
        self.player_sprite.draw()

    def on_key_press(self, key, modifiers):
        """ Maneja la entrada del teclado para mover a Pac-Man """
        if key == arcade.key.UP:
            self.player_sprite.change_y = 5
            self.player_sprite.texture = arcade.load_texture(os.path.join(SPRITE_PATH, "pacman-up/1.png"))
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -5
            self.player_sprite.texture = arcade.load_texture(os.path.join(SPRITE_PATH, "pacman-down/1.png"))
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -5
            self.player_sprite.texture = arcade.load_texture(os.path.join(SPRITE_PATH, "pacman-left/1.png"))
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = 5
            self.player_sprite.texture = arcade.load_texture(os.path.join(SPRITE_PATH, "pacman-right/1.png"))

    def on_key_release(self, key, modifiers):
        """ Detiene el movimiento cuando se suelta la tecla """
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.player_sprite.change_y = 0
        elif key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Actualiza el estado del juego """
        self.physics_engine.update()


if __name__ == "__main__":
    game = PacManGame()
    game.setup()
    arcade.run()
