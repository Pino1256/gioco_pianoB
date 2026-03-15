import arcade
from sfondo import Parallax

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

        #sfondo
        self.sfondo_parallax = Parallax()

        #gravita
        self.physics_engine = 0

        # movimento
        self.left_pressed = False
        self.right_pressed = False

        #camera
        self.camera = arcade.camera.Camera2D()

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
        lungezza = 20000
        self.floor = arcade.SpriteSolidColor(lungezza, 20, arcade.color.GREEN)
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

        self.camera.use()

        self.sfondo_parallax.backgrounds.pos = self.camera.position
        self.sfondo_parallax.backgrounds.draw()

        self.lista_pavimento.draw()
        self.lista_player.draw()
    
    def on_update(self, delta_time):
        
        self.player.change_x = 0

        if self.left_pressed:
            self.player.change_x -= self.speed
        if self.right_pressed:
            self.player.change_x += self.speed
        
        if self.player.change_x < 0: 
            self.player.scale = (-1*self.scale, self.scale)
        elif self.player.change_x > 0:
            self.player.scale = (self.scale, self.scale)
        
        # target_x = self.player.center_x
        # target_y = SCREEN_HEIGHT / 2

        # self.camera.position = (target_x, target_y)

        self.physics_engine.update()

        SCHERMO_CENTRO_X = SCREEN_WIDTH / 2
        MARGINE_LATERALE = 50

        limite_sinistro = self.camera.position.x - SCHERMO_CENTRO_X + MARGINE_LATERALE
        limite_destro = self.camera.position.x + SCHERMO_CENTRO_X - MARGINE_LATERALE

        nuova_pos_x = self.camera.position.x

        if self.player.center_x > limite_destro:
            nuova_pos_x += self.player.center_x - limite_destro
        elif self.player.center_x < limite_sinistro:
            nuova_pos_x -= limite_sinistro - self.player.center_x
        
        self.camera.position = (nuova_pos_x, self.camera.position.y)

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