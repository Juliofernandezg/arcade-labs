import arcade
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Step and Collect Game"


class ShopView(arcade.View):
    def __init__(self, game_view):
        super().__init__()
        self.game_view = game_view
        self.upgrade_button_x = SCREEN_WIDTH // 2
        self.upgrade_button_y = SCREEN_HEIGHT // 2
        self.companion_button_x = SCREEN_WIDTH // 2
        self.companion_button_y = SCREEN_HEIGHT // 2 - 100
        self.button_width = 150
        self.button_height = 50

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Shop", SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT - 50, arcade.color.BLACK, 24)

        # Upgrade button
        arcade.draw_rectangle_filled(self.upgrade_button_x, self.upgrade_button_y, self.button_width,
                                     self.button_height, arcade.color.BLUE)
        arcade.draw_text("Upgrade", self.upgrade_button_x - 40, self.upgrade_button_y - 10, arcade.color.WHITE, 14)
        arcade.draw_text(f"Cost: {self.game_view.upgrade_cost} Coins", SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 60,
                         arcade.color.BLACK, 16)

        # Companion button
        arcade.draw_rectangle_filled(self.companion_button_x, self.companion_button_y, self.button_width,
                                     self.button_height, arcade.color.GREEN)
        arcade.draw_text("Buy Companion", self.companion_button_x - 60, self.companion_button_y - 10,
                         arcade.color.WHITE, 14)
        arcade.draw_text(f"Cost: {self.game_view.companion_cost} Coins", SCREEN_WIDTH // 2 - 50,
                         SCREEN_HEIGHT // 2 - 40, arcade.color.BLACK, 16)

    def on_mouse_press(self, x, y, button, modifiers):
        if (self.upgrade_button_x - self.button_width // 2 < x < self.upgrade_button_x + self.button_width // 2 and
                self.upgrade_button_y - self.button_height // 2 < y < self.upgrade_button_y + self.button_height // 2):
            self.game_view.upgrade()
            self.window.show_view(self.game_view)
        elif (
                self.companion_button_x - self.button_width // 2 < x < self.companion_button_x + self.button_width // 2 and
                self.companion_button_y - self.button_height // 2 < y < self.companion_button_y + self.button_height // 2):
            self.game_view.buy_companion()
            self.window.show_view(self.game_view)


class StepGame(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.SKY_BLUE

        # Load character sprite
        self.character = arcade.Sprite(
            ":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", 0.5)
        self.character.center_x = SCREEN_WIDTH // 2
        self.character.center_y = SCREEN_HEIGHT // 2

        # Companions
        self.companions = []
        self.companion_count = 0
        self.companion_cost = 10000

        # Coin counter
        self.coin_count = 0
        self.floor_count = 1
        self.upgrade_cost = 10
        self.min_coin_reward = 1
        self.max_coin_reward = 5

        # Step button properties
        self.button_x = SCREEN_WIDTH // 2
        self.button_y = 100
        self.button_width = 200
        self.button_height = 50

        # Shop button
        self.shop_button_x = SCREEN_WIDTH - 100
        self.shop_button_y = 50

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(self.background_color)

        # Draw character
        self.character.draw()

        # Draw companions
        for companion in self.companions:
            companion.draw()

        # Draw step button
        arcade.draw_rectangle_filled(self.button_x, self.button_y, self.button_width, self.button_height,
                                     arcade.color.DARK_GREEN)
        arcade.draw_text("Step Forward", self.button_x - 60, self.button_y - 10, arcade.color.WHITE, 14)

        # Draw coin counter and floor count
        arcade.draw_text(f"Coins: {self.coin_count}", SCREEN_WIDTH - 150, SCREEN_HEIGHT - 50, arcade.color.BLACK, 20)
        arcade.draw_text(f"Floor: {self.floor_count}", 50, SCREEN_HEIGHT - 50, arcade.color.BLACK, 20)

        # Draw shop button
        arcade.draw_rectangle_filled(self.shop_button_x, self.shop_button_y, 100, 40, arcade.color.RED)
        arcade.draw_text("Shop", self.shop_button_x - 20, self.shop_button_y - 10, arcade.color.WHITE, 14)

    def change_background(self):
        self.background_color = random.choice(
            [arcade.color.LIGHT_BLUE, arcade.color.LIGHT_GREEN, arcade.color.LIGHT_PINK, arcade.color.LIGHT_YELLOW])
        self.floor_count += 1

    def upgrade(self):
        if self.coin_count >= self.upgrade_cost:
            self.coin_count -= self.upgrade_cost
            self.min_coin_reward += 1
            self.max_coin_reward += 1
            self.upgrade_cost = int(self.upgrade_cost * 1.5)

    def on_mouse_press(self, x, y, button, modifiers):
        if (self.button_x - self.button_width // 2 < x < self.button_x + self.button_width // 2 and
                self.button_y - self.button_height // 2 < y < self.button_y + self.button_height // 2):
            self.step_forward()
        elif (self.shop_button_x - 50 < x < self.shop_button_x + 50 and
              self.shop_button_y - 20 < y < self.shop_button_y + 20):
            self.window.show_view(ShopView(self))

    def step_forward(self):
        self.character.center_x += 20
        coins_gained = random.randint(self.min_coin_reward, self.max_coin_reward)
        self.coin_count += coins_gained * (2 ** self.companion_count)
        if self.character.center_x >= SCREEN_WIDTH:
            self.character.center_x = 0
            self.change_background()


if __name__ == "__main__":
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = StepGame()
    window.show_view(start_view)
    arcade.run()