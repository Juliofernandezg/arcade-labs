import arcade

# Dimensiones de la ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CAR_SPEED = 2
CLOUD_SPEED = 0.5
BIRD_SPEED = 1.5


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


class Cloud:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, 30, arcade.color.LIGHT_GRAY)
        arcade.draw_circle_filled(self.x + 20, self.y + 10, 25, arcade.color.LIGHT_GRAY)
        arcade.draw_circle_filled(self.x - 20, self.y + 10, 25, arcade.color.LIGHT_GRAY)
        arcade.draw_circle_filled(self.x + 40, self.y, 20, arcade.color.LIGHT_GRAY)
        arcade.draw_circle_filled(self.x - 40, self.y, 20, arcade.color.LIGHT_GRAY)

    def update(self):
        self.x += CLOUD_SPEED
        if self.x > SCREEN_WIDTH + 50:
            self.x = -50


class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        arcade.draw_arc_outline(self.x - 10, self.y, 20, 10, arcade.color.BLACK, 0, 180, 2)
        arcade.draw_arc_outline(self.x + 10, self.y, 20, 10, arcade.color.BLACK, 0, 180, 2)

    def update(self):
        self.x += BIRD_SPEED
        if self.x > SCREEN_WIDTH + 20:
            self.x = -20


class CityWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Ciudad con coches animados")
        arcade.set_background_color(arcade.color.AERO_BLUE)
        self.cars = [
            Car(150, 80, arcade.color.RED, arcade.color.DARK_RED),
            Car(400, 120, arcade.color.BLUE, arcade.color.DARK_BLUE),
            Car(650, 90, arcade.color.YELLOW, arcade.color.ORANGE)
        ]
        self.clouds = [
            Cloud(150, 550),
            Cloud(350, 520),
            Cloud(600, 540),
            Cloud(700, 500),
            Cloud(500, 560)
        ]
        self.birds = [
            Bird(100, 550),
            Bird(200, 500),
            Bird(300, 540),
            Bird(500, 530),
            Bird(700, 520)
        ]

    def on_draw(self):
        arcade.start_render()
        # Dibujar el suelo (calle)
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 150, 0, arcade.color.DIM_GRAY)
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 130, 50, arcade.color.BLACK)

        # Dibujar sol
        arcade.draw_circle_filled(780, 550, 90, arcade.color.SUNSET)

        # Dibujar nubes
        for cloud in self.clouds:
            cloud.draw()

        # Dibujar gaviotas
        for bird in self.birds:
            bird.draw()

        # Dibujar coches
        for car in self.cars:
            car.draw()

    def update(self, delta_time):
        for car in self.cars:
            car.update()
        for cloud in self.clouds:
            cloud.update()
        for bird in self.birds:
            bird.update()


if __name__ == "__main__":
    window = CityWindow()
    arcade.run()