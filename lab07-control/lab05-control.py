import arcade
import random

# --- Constants ---
SCREEN_WIDTH = 800  # Ancho de la ventana del juego, define el área horizontal del juego.
SCREEN_HEIGHT = 600  # Alto de la ventana del juego, define el área vertical del juego.
CAR_ACCELERATION = 0.2  # Cantidad de aceleración aplicada al coche cuando se mueve.
CAR_FRICTION = 0.05  # Fricción que reduce la velocidad del coche con el tiempo para evitar deslizamientos.
CAR_MAX_SPEED = 4  # Velocidad máxima que puede alcanzar el coche para evitar movimientos excesivos.
OBSTACLE_INITIAL_SPEED = 3  # Velocidad inicial con la que los obstáculos se moverán hacia abajo.
OBSTACLE_SPEED_INCREMENT = 0.1  # Cantidad en la que la velocidad de los obstáculos aumenta con el tiempo.
OBSTACLE_SPAWN_RATE = 2  # Intervalo de tiempo (en segundos) entre la aparición de nuevos obstáculos.
LIVES = 3  # Número inicial de vidas del jugador, decrece con cada colisión.


class Car:
    def __init__(self, x, y):
        # Inicialización del coche con posición y características visuales.
        self.x = x  # Posición horizontal del coche en la pantalla.
        self.y = y  # Posición vertical del coche en la pantalla.
        self.color = arcade.color.RED  # Color del cuerpo del coche.
        self.roof_color = arcade.color.DARK_RED  # Color del techo del coche.
        self.width = 80  # Ancho del coche en píxeles.
        self.height = 40  # Altura del coche en píxeles.
        self.roof_width = 50  # Ancho del techo en píxeles.
        self.roof_height = 30  # Altura del techo en píxeles.
        self.wheel_radius = 10  # Radio de las ruedas del coche.
        self.change_x = 0  # Velocidad de cambio en el eje X.
        self.change_y = 0  # Velocidad de cambio en el eje Y.

    def draw(self):
        # Dibuja el coche en pantalla utilizando rectángulos y círculos para simular la forma de un coche.
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color)
        arcade.draw_rectangle_filled(self.x, self.y + 20, self.roof_width, self.roof_height, self.roof_color)
        arcade.draw_circle_filled(self.x - 25, self.y - 15, self.wheel_radius, arcade.color.BLACK)
        arcade.draw_circle_filled(self.x + 25, self.y - 15, self.wheel_radius, arcade.color.BLACK)

    def update_position(self):
        # Aplica fricción al coche para reducir la velocidad con el tiempo.
        self.change_x *= (1 - CAR_FRICTION)
        self.change_y *= (1 - CAR_FRICTION)

        # Modifica la posición del coche en base a su velocidad actual.
        self.x += self.change_x
        self.y += self.change_y

        # Define los límites de la carretera para que el coche no salga de ella.
        road_left = 100  # Límite izquierdo de la carretera.
        road_right = SCREEN_WIDTH - 100  # Límite derecho de la carretera.
        road_bottom = 50  # Límite inferior de la carretera.
        road_top = 130  # Límite superior de la carretera.

        # Asegura que el coche permanezca dentro de los límites de la carretera.
        if self.x < road_left:
            self.x = road_left
        elif self.x > road_right:
            self.x = road_right

        if self.y < road_bottom:
            self.y = road_bottom
        elif self.y > road_top:
            self.y = road_top


class Obstacle:
    def __init__(self, x, y, speed):
        # Inicializa un obstáculo con posición y velocidad específicas.
        self.x = x  # Posición horizontal del obstáculo.
        self.y = y  # Posición vertical del obstáculo.
        self.width = 50  # Ancho del obstáculo.
        self.height = 50  # Altura del obstáculo.
        self.speed = speed  # Velocidad a la que se mueve el obstáculo.

    def draw(self):
        # Dibuja el obstáculo como un rectángulo azul en pantalla.
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, arcade.color.BLUE)

    def update(self):
        # Mueve el obstáculo hacia abajo en la pantalla.
        self.y -= self.speed


class MyGame(arcade.Window):
    def __init__(self):
        # Configura la ventana principal del juego y sus características.
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.set_update_rate(1 / 60)  # Ajusta la velocidad de actualización del juego a 60 FPS.
        self.setup()

    def setup(self):
        # Configuración inicial del juego al iniciarlo o reiniciarlo.
        self.car = Car(SCREEN_WIDTH // 2, 100)  # Crea un coche en la posición inicial.
        self.obstacles = []  # Lista de obstáculos en pantalla.
        self.time_since_last_obstacle = 0  # Contador para gestionar la aparición de obstáculos.
        self.lives = LIVES  # Número de vidas del jugador.
        self.obstacle_speed = OBSTACLE_INITIAL_SPEED  # Velocidad inicial de los obstáculos.

    def increase_obstacle_speed(self):
        # Aumenta la velocidad de los obstáculos con cada nuevo obstáculo generado.
        self.obstacle_speed += OBSTACLE_SPEED_INCREMENT

    def on_draw(self):
        # Renderiza los elementos visuales en la pantalla.
        self.clear()
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 150, 0, arcade.color.DIM_GRAY)
        arcade.draw_lrtb_rectangle_filled(100, SCREEN_WIDTH - 100, 130, 50, arcade.color.BLACK)
        self.car.draw()
        for obstacle in self.obstacles:
            obstacle.draw()

        # Dibuja el número de vidas del jugador en la pantalla.
        arcade.draw_text(f"Vidas: {self.lives}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 20)

    def on_update(self, delta_time):
        # Lógica de actualización del juego en cada fotograma.
        self.car.update_position()
        self.time_since_last_obstacle += delta_time
        if self.time_since_last_obstacle > OBSTACLE_SPAWN_RATE:
            obstacle_x = random.randint(150, SCREEN_WIDTH - 150)
            obstacle_y = SCREEN_HEIGHT + 50
            self.obstacles.append(Obstacle(obstacle_x, obstacle_y, self.obstacle_speed))
            self.time_since_last_obstacle = 0
            self.increase_obstacle_speed()

        for obstacle in self.obstacles:
            obstacle.update()
        self.obstacles = [obs for obs in self.obstacles if obs.y > 0]

    def on_key_press(self, key, modifiers):
        # Maneja la entrada del teclado para controlar el coche.
        if key == arcade.key.LEFT:
            self.car.change_x -= CAR_ACCELERATION
        elif key == arcade.key.RIGHT:
            self.car.change_x += CAR_ACCELERATION
        elif key == arcade.key.UP:
            self.car.change_y += CAR_ACCELERATION
        elif key == arcade.key.DOWN:
            self.car.change_y -= CAR_ACCELERATION

    def on_key_release(self, key, modifiers):
        # Detiene el movimiento del coche cuando se sueltan las teclas.
        if key in (arcade.key.LEFT, arcade.key.RIGHT):
            self.car.change_x = 0
        elif key in (arcade.key.UP, arcade.key.DOWN):
            self.car.change_y = 0


def main():
    # Función principal que inicia el juego.
    window = MyGame()
    arcade.run()


main()
