import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        
        arcade.set_background_color(arcade.color.DARK_GREEN)

        #player
        self.lista_player = arcade.SpriteList()
        self.player = None
        self.speed: int = 5
        self.scale = 0.11
        self.player_jump_speed = 20

        #pavimento
        self.lista_pavimento = arcade.SpriteList()

        #gravita
        self.physics_engine = 0

        # movimento
        self.left_pressed = False
        self.right_pressed = False

        self.setup()
        self.pavimento()
        self.CreGravita()
    
    def setup(self): # player

        self.player = arcade.Sprite("./assets/player.png")
        self.player.center_x = 300
        self.player.center_y = 100
        self.player.scale = self.scale
        self.lista_player.append(self.player)
    
    def pavimento(self):
        self.floor = arcade.SpriteSolidColor(SCREEN_WIDTH, 20, arcade.color.GREEN)
        self.floor.center_x = SCREEN_WIDTH / 2
        self.floor.center_y = 10 #posizionamento sul fondo
        self.floor.visible = False

        self.lista_pavimento.append(self.floor)
    
    def CreGravita(self):
        self.gravita = 1.0
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player,
            gravity_constant = self.gravita,
            walls = self.lista_pavimento
        )

    def on_draw(self):
        self.clear()

        self.lista_pavimento.draw()
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

        self.physics_engine.update()

    def on_key_press(self, tasto, modificatori):

        if tasto in (arcade.key.LEFT, arcade.key.A):
            self.left_pressed = True
        elif tasto in (arcade.key.RIGHT, arcade.key.D):
            self.right_pressed = True        
        elif tasto == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player.change_y = self.player_jump_speed

    def on_key_release(self, tasto, modificatori):

        """Gestisce il rilascio dei tasti"""

        if tasto in (arcade.key.LEFT, arcade.key.A):
            self.left_pressed = False
        elif tasto in (arcade.key.RIGHT, arcade.key.D):
            self.right_pressed = False  