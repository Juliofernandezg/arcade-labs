import arcade

# Dimensiones de la ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CAR_SPEED = 2


class Car:
    def __init__(self, x, y, color, roof_color):
        self.x = x
        self.y = y
        self.color = color
        self.roof_color = roof_color
        self.width = 80
        self.height = 40
        self.roof_width = 50
        self.roof_height = 30
        self.wheel_radius = 10

    def draw(self):
        # Dibujar cuerpo del coche
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)
        arcade.draw_rectangle_filled(self.x, self.y + 20, self.roof_width, self.roof_height, self.roof_color)
        # Dibujar ruedas
        arcade.draw_circle_filled(self.x - 25, self.y - 15, self.wheel_radius, arcade.color.BLACK)
        arcade.draw_circle_filled(self.x - 25, self.y - 15, self.wheel_radius // 2, arcade.color.GRAY)
        arcade.draw_circle_filled(self.x + 25, self.y - 15, self.wheel_radius, arcade.color.BLACK)
        arcade.draw_circle_filled(self.x + 25, self.y - 15, self.wheel_radius // 2, arcade.color.GRAY)

    def update(self):
        self.x += CAR_SPEED
        if self.x > SCREEN_WIDTH + self.width:
            self.x = -self.width


class CityWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Ciudad con coches animados")
        arcade.set_background_color(arcade.color.AERO_BLUE)
        self.cars = [
            Car(150, 80, arcade.color.RED, arcade.color.DARK_RED),
            Car(400, 120, arcade.color.BLUE, arcade.color.DARK_BLUE),
            Car(650, 90, arcade.color.YELLOW, arcade.color.ORANGE)
        ]

    def on_draw(self):
        arcade.start_render()
        # Dibujar el suelo (calle)
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 150, 0, arcade.color.DIM_GRAY)
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 130, 50, arcade.color.BLACK)

        # Dibujar sol
        arcade.draw_circle_filled(780, 550, 90, arcade.color.SUNSET)

        # Dibujar coches
        for car in self.cars:
            car.draw()

    def update(self, delta_time):
        for car in self.cars:
            car.update()


if __name__ == "__main__":
    window = CityWindow()
    arcade.run()
