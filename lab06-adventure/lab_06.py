class Room:
    def __init__(self, description, north=None, east=None, south=None, west=None):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    # Lista de habitaciones
    room_list = []

    # Definición de las habitaciones
    room_list.append(
        Room("Estás en una habitación polvorienta del castillo.\nPasajes llevan al norte y al sur.", north=1, south=2))
    room_list.append(Room("Estás en la armería.\nHay una habitación al sur.", south=0))
    room_list.append(
        Room("Estás en un pasillo iluminado por antorchas.\nHay habitaciones al este y oeste.", east=3, west=4))
    room_list.append(
        Room("Estás en un dormitorio. Una ventana da al patio del castillo.\nUn pasillo está al oeste.", west=2))
    room_list.append(
        Room("Estás en la cocina. Parece que están preparando un asado para la cena.\nUn pasillo está al este.",
             east=2))

    # Inicio del juego
    current_room = 0
    done = False

    while not done:
        print("\n" + room_list[current_room].description)
        direction = input("¿Hacia dónde quieres ir? (n/e/s/o para salir escribe 'salir'): ").strip().lower()

        if direction in ["n", "norte"]:
            next_room = room_list[current_room].north
        elif direction in ["e", "este"]:
            next_room = room_list[current_room].east
        elif direction in ["s", "sur"]:
            next_room = room_list[current_room].south
        elif direction in ["o", "oeste"]:
            next_room = room_list[current_room].west
        elif direction == "salir":
            print("Has salido del juego.")
            break
        else:
            print("No entiendo esa dirección.")
            continue

        if next_room is None:
            print("No puedes ir en esa dirección.")
        else:
            current_room = next_room


if __name__ == "__main__":
    main()
