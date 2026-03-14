import arcade

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        
        arcade.set_background_color(arcade.color.DARK_GREEN)

        self.lista_player = arcade.SpriteList()
        self.player = None
        self.speed: int = 5
        self.scale = 0.11

        # movimento
        self.left_pressed = False
        self.right_pressed = False

        self.setup()
    
    def setup(self): # player

        self.player = arcade.Sprite("./assets/player.png")
        self.player.center_x = 300
        self.player.center_y = 100
        self.player.scale = self.scale
        self.lista_player.append(self.player)
    
    def on_draw(self):
        self.clear()
        self.lista_player.draw()
    
    def on_update(self, delta_time):
        
        change_x = 0
        change_y = 0

        if self.left_pressed:
            change_x -= self.speed
        if self.right_pressed:
            change_x += self.speed

        # Applica movimento
        self.player.center_x += change_x
        self.player.center_y += change_y
        
        if change_x < 0: 
            self.player.scale = (-1*self.scale, self.scale)
        elif change_x > 0:
            self.player.scale = (self.scale, self.scale)

    def on_key_press(self, tasto, modificatori):

        if tasto in (arcade.key.LEFT, arcade.key.A):
            self.left_pressed = True
        elif tasto in (arcade.key.RIGHT, arcade.key.D):
            self.right_pressed = True          

    def on_key_release(self, tasto, modificatori):

        """Gestisce il rilascio dei tasti"""

        if tasto in (arcade.key.LEFT, arcade.key.A):
            self.left_pressed = False
        elif tasto in (arcade.key.RIGHT, arcade.key.D):
            self.right_pressed = False  