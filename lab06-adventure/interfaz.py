import arcade
import PySimpleGUI as sg

class GameInterface:
    def __init__(self, game):
        self.game = game
        self.combat_active = False
        self.current_enemy = None

    def draw(self):
        """Dibuja la interfaz en pantalla."""
        if self.combat_active:
            arcade.draw_text("¡Combate en curso!", 10, 560, arcade.color.WHITE, 16)

    def show_combat_menu(self, enemy):
        """Muestra el menú de combate usando PySimpleGUI."""
        self.combat_active = True
        self.current_enemy = enemy

        layout = [
            [sg.Text("¡Has encontrado un enemigo! ¿Qué quieres hacer?")],
            [sg.Button("Atacar"), sg.Button("Usar Objeto"), sg.Button("Huir")]
        ]

        window = sg.Window("Combate", layout)

        while True:
            event, _ = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Atacar":
                self.game.player.attack([self.current_enemy])
                if self.current_enemy.health <= 0:
                    loot = self.current_enemy.drop_loot()
                    if loot:
                        self.game.player.inventory.append(loot)
                        print(f"Recogiste {loot.name}!")
                    self.combat_active = False
                    window.close()
                    break
                self.current_enemy.attack(self.game.player)
            elif event == "Usar Objeto":
                self.show_inventory_menu()
            elif event == "Huir":
                print("Has huido del combate!")
                self.combat_active = False
                window.close()
                break

        window.close()

    def show_inventory_menu(self):
        """Muestra el inventario y permite usar objetos."""
        inventory_list = [item.name for item in self.game.player.inventory]
        layout = [[sg.Listbox(values=inventory_list, size=(30, 10), key="ITEM")],
                  [sg.Button("Usar"), sg.Button("Cerrar")]]
        window = sg.Window("Inventario", layout)

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == "Cerrar":
                break
            elif event == "Usar" and values["ITEM"]:
                item_name = values["ITEM"][0]
                item = next((i for i in self.game.player.inventory if i.name == item_name), None)
                if item:
                    self.game.player.use_item(item)
                    self.game.player.inventory.remove(item)
                    window.close()
                    break

        window.close()