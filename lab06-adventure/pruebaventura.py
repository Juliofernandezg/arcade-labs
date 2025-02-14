import random


class Room:
    def __init__(self, description, north=None, east=None, south=None, west=None, up=None, down=None, items=None,
                 enemy=None):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.items = items if items else []
        self.enemy = enemy


class Player:
    def __init__(self):
        self.health = 100
        self.inventory = []
        self.current_room = 0

    def pick_up(self, item):
        self.inventory.append(item)
        print(f"Has recogido {item}.")

    def attack(self, enemy):
        damage = random.randint(5, 20)
        print(f"Has atacado a {enemy} y le has hecho {damage} de daño.")


def main():
    # Lista de habitaciones
    room_list = []
    room_list.append(
        Room("Estás en una gran sala con un trono dorado. Pasajes al norte, este y sur.", north=1, east=3, south=2))
    room_list.append(Room("Estás en una biblioteca antigua llena de libros de magia. Pasajes al sur.", south=0,
                          items=["Libro de hechizos"]))
    room_list.append(Room("Estás en un oscuro calabozo con cadenas oxidadas. Hay una puerta al norte.", north=0,
                          items=["Llave dorada"], enemy="Esqueleto"))
    room_list.append(
        Room("Estás en una armería repleta de armas. Hay una puerta al oeste.", west=0, items=["Espada legendaria"]))

    player = Player()
    done = False

    while not done:
        current_room = room_list[player.current_room]
        print("\n" + current_room.description)
        if current_room.items:
            print(f"Objetos en la habitación: {', '.join(current_room.items)}")
        if current_room.enemy:
            print(f"¡Cuidado! Hay un {current_room.enemy} aquí.")

        command = input("¿Qué quieres hacer? (n/e/s/o/tomar/atacar/salir): ").strip().lower()

        if command in ["n", "norte"]:
            next_room = current_room.north
        elif command in ["e", "este"]:
            next_room = current_room.east
        elif command in ["s", "sur"]:
            next_room = current_room.south
        elif command in ["o", "oeste"]:
            next_room = current_room.west
        elif command == "tomar":
            if current_room.items:
                item = current_room.items.pop()
                player.pick_up(item)
            else:
                print("No hay nada que tomar aquí.")
            continue
        elif command == "atacar":
            if current_room.enemy:
                player.attack(current_room.enemy)
            else:
                print("No hay nadie a quien atacar aquí.")
            continue
        elif command == "salir":
            print("Has salido del juego.")
            break
        else:
            print("No entiendo esa acción.")
            continue

        if next_room is None:
            print("No puedes ir en esa dirección.")
        else:
            player.current_room = next_room


if __name__ == "__main__":
    main()
