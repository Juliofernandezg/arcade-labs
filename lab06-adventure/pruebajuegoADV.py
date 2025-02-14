import random
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Aventura Oscura"


class Room:
    def __init__(self, description, north=None, east=None, south=None, west=None, items=None, enemy=None):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.items = items if items else []
        self.enemy = enemy
        self.enemy_health = 100 if enemy == "Boss" else 50 if enemy else 0

    def enemy_attack(self, player):
        if self.enemy and self.enemy_health > 0:
            damage = random.randint(5, 15)
            player.health -= damage
            print(f"{self.enemy} te ha atacado y te ha hecho {damage} de daño.")
            if player.health <= 0:
                print("Has sido derrotado. Fin del juego.")
                arcade.close_window()


class Player:
    def __init__(self):
        self.health = 100
        self.attack_power = 10
        self.inventory = ["pocion", "pocion", "pocion"]  # Empieza con 3 pociones
        self.current_room = 0
        self.sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.7)
        self.sprite.center_x = SCREEN_WIDTH // 2
        self.sprite.center_y = SCREEN_HEIGHT // 4

    def pick_up(self, item):
        if item == "pocion":
            self.inventory.append(item)
            print("Has recogido una poción.")
        elif item == "espada":
            self.attack_power += 5
            print("Tu ataque ha aumentado en 5 puntos.")

    def attack(self, room):
        if room.enemy and room.enemy_health > 0:
            damage = random.randint(5, 20) + self.attack_power
            room.enemy_health -= damage
            print(f"Has atacado a {room.enemy} y le has hecho {damage} de daño.")
            if room.enemy_health <= 0:
                print(f"Has derrotado a {room.enemy}.")
                room.enemy = None
                room.enemy_health = 0
        room.enemy_attack(self)

    def drink_potion(self):
        if "pocion" in self.inventory:
            self.health += 30
            self.inventory.remove("pocion")
            print("Has tomado una poción y recuperado 30 puntos de salud.")
        else:
            print("No tienes pociones.")


class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.backgrounds = [":resources:images/backgrounds/abstract_1.jpg",
                            ":resources:images/backgrounds/abstract_2.jpg"]
        self.current_bg = random.choice(self.backgrounds)
        self.player = Player()
        self.rooms = self.create_rooms()
        self.enemy_sprites = {
            "Bee": ":resources:images/enemies/bee.png",
            "FishGreen": ":resources:images/enemies/fishGreen.png",
            "FishPink": ":resources:images/enemies/fishPink.png",
            "Fly": ":resources:images/enemies/fly.png",
            "Frog": ":resources:images/enemies/frog.png",
            "Ladybug": ":resources:images/enemies/ladybug.png",
            "Mouse": ":resources:images/enemies/mouse.png",
            "SlimeBlue": ":resources:images/enemies/slimeBlue.png",
            "SlimeGreen": ":resources:images/enemies/slimeGreen.png",
            "WormPink": ":resources:images/enemies/wormPink.png",
            "Boss": ":resources:images/enemies/saw.png"
        }

    def create_rooms(self):
        rooms = []
        for i in range(50):
            rooms.append(Room(f"Estás en la sala {i}. Pasajes aleatorios a distintas direcciones.",
                              north=random.randint(0, 49),
                              east=random.randint(0, 49),
                              south=random.randint(0, 49),
                              west=random.randint(0, 49),
                              items=["pocion", "espada", "llave dorada" if i == 25 else None],
                              enemy=random.choice(
                                  ["Bee", "FishGreen", "FishPink", "Fly", "Frog", "Ladybug", "Mouse", "SlimeBlue",
                                   "SlimeGreen", "WormPink", None])))
        rooms.append(Room("Estás en la sala del Jefe Final. Prepárate para la batalla.", enemy="Boss"))
        return rooms

    def on_draw(self):
        arcade.start_render()
        bg = arcade.load_texture(self.current_bg)
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, bg)
        arcade.draw_text(self.rooms[self.player.current_room].description, 50, 500, arcade.color.WHITE, 14)
        self.player.sprite.draw()

        room = self.rooms[self.player.current_room]
        if room.enemy:
            enemy_sprite = arcade.Sprite(self.enemy_sprites[room.enemy], 0.5)
            enemy_sprite.center_x = SCREEN_WIDTH // 2
            enemy_sprite.center_y = SCREEN_HEIGHT // 2
            enemy_sprite.draw()

    def on_key_press(self, key, modifiers):
        room = self.rooms[self.player.current_room]
        if key == arcade.key.SPACE and room.enemy:
            self.player.attack(room)
        elif key == arcade.key.P:
            self.player.drink_potion()
        elif not room.enemy:
            if key == arcade.key.UP and room.north:
                self.player.current_room = room.north
            elif key == arcade.key.RIGHT and room.east:
                self.player.current_room = room.east
            elif key == arcade.key.DOWN and room.south:
                self.player.current_room = room.south
            elif key == arcade.key.LEFT and room.west:
                self.player.current_room = room.west
            self.current_bg = random.choice(self.backgrounds)


if __name__ == "__main__":
    window = GameWindow()
    arcade.run()