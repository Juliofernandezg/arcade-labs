import arcade

# Dimensiones de la ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Abrir una ventana
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Ciudad con coches")

# Establecer el color de fondo
arcade.set_background_color(arcade.color.AERO_BLUE)

# Iniciar el renderizado
arcade.start_render()

# --- Dibujar el suelo (calle) ---
arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 150, 0, arcade.color.DIM_GRAY)
arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 130, 50, arcade.color.BLACK)

#sol
arcade.draw_circle_filled(780, 550, 90, arcade.color.SUNSET)
# --- Dibujar nubes ---
def draw_cloud(x, y):
    arcade.draw_circle_filled(x, y, 30, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(x + 20, y + 10, 25, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(x - 20, y + 10, 25, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(x + 40, y, 20, arcade.color.LIGHT_GRAY)
    arcade.draw_circle_filled(x - 40, y, 20, arcade.color.LIGHT_GRAY)

draw_cloud(150, 550)
draw_cloud(350, 520)
draw_cloud(600, 540)

draw_cloud(700, 500)

draw_cloud(500, 560)
def draw_bird(x, y):
    arcade.draw_arc_outline(x - 10, y, 20, 10, arcade.color.BLACK, 0, 180, 2)
    arcade.draw_arc_outline(x + 10, y, 20, 10, arcade.color.BLACK, 0, 180, 2)

draw_bird(100, 550)
draw_bird(200, 500)
draw_bird(300, 540)
draw_bird(500, 530)
draw_bird(700, 520)


# --- Dibujar edificios ---
arcade.draw_lrtb_rectangle_filled(50, 210, 500, 150, arcade.color.BRICK_RED)
arcade.draw_lrtb_rectangle_filled(110, 150, 180, 150, arcade.color.GRAY)
arcade.draw_lrtb_rectangle_filled(250, 410, 550, 150, arcade.color.DARK_BLUE)
arcade.draw_lrtb_rectangle_filled(310, 350, 180, 150, arcade.color.GRAY)
arcade.draw_lrtb_rectangle_filled(450, 610, 490, 150, arcade.color.DARK_GREEN)
arcade.draw_lrtb_rectangle_filled(510, 550, 180, 150, arcade.color.GRAY)
arcade.draw_lrtb_rectangle_filled(650, 780, 500, 150, arcade.color.DARK_GRAY)
arcade.draw_lrtb_rectangle_filled(690, 730, 180, 150, arcade.color.GRAY)

# Ventanas de los edificios
for x in range(70, 200, 40):
    for y in range(220, 500, 60):
        arcade.draw_rectangle_filled(x, y, 20, 30, arcade.color.LIGHT_YELLOW)
for x in range(270, 400, 40):
    for y in range(220, 550, 60):
        arcade.draw_rectangle_filled(x, y, 20, 30, arcade.color.LIGHT_YELLOW)
for x in range(470, 600, 40):
    for y in range(220, 480, 60):
        arcade.draw_rectangle_filled(x, y, 20, 30, arcade.color.LIGHT_YELLOW)
for x in range(670, 780, 40):
    for y in range(220, 520, 60):
        arcade.draw_rectangle_filled(x, y, 20, 30, arcade.color.LIGHT_YELLOW)

# --- Dibujar coches ---
# Coche 1
arcade.draw_rectangle_filled(150, 80, 80, 40, arcade.color.RED)
arcade.draw_rectangle_filled(150, 100, 50, 30, arcade.color.DARK_RED)
arcade.draw_circle_filled(125, 65, 10, arcade.color.BLACK)
arcade.draw_circle_filled(125, 65, 5, arcade.color.GRAY)
arcade.draw_circle_filled(175, 65, 10, arcade.color.BLACK)
arcade.draw_circle_filled(175, 65, 5, arcade.color.GRAY)

# Coche 2
arcade.draw_rectangle_filled(400, 120, 80, 40, arcade.color.BLUE)
arcade.draw_rectangle_filled(400, 140, 50, 30, arcade.color.DARK_BLUE)
arcade.draw_circle_filled(375, 105, 10, arcade.color.BLACK)
arcade.draw_circle_filled(375, 105, 5, arcade.color.GRAY)
arcade.draw_circle_filled(425, 105, 10, arcade.color.BLACK)
arcade.draw_circle_filled(425, 105, 5, arcade.color.GRAY)

# Coche 3
arcade.draw_rectangle_filled(650, 90, 80, 40, arcade.color.YELLOW)
arcade.draw_rectangle_filled(650, 110, 50, 30, arcade.color.ORANGE)
arcade.draw_circle_filled(625, 75, 10, arcade.color.BLACK)
arcade.draw_circle_filled(625, 75, 5, arcade.color.GRAY)
arcade.draw_circle_filled(675, 75, 10, arcade.color.BLACK)
arcade.draw_circle_filled(675, 75, 5, arcade.color.GRAY)


# Terminar de dibujar
arcade.finish_render()

# Mantener la ventana abierta hasta que se cierre
arcade.run()
