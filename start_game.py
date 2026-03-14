import arcade
from menuview import MenuView

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class StartGioco(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "THE GAME")
        pass
        menu = MenuView()
        self.show_view(menu)

def main():
    widow = StartGioco()
    arcade.run()

if __name__ == "__main__":
    main()