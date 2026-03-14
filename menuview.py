import arcade

class MenuView (arcade.View):
    def on_draw(self):
        self.clear()

        arcade.draw_text("IL GIOCO CHE SALTA I GIOCHI", 480, 350,
                         arcade.color.CYBER_YELLOW, font_size=48, anchor_x="center")

        arcade.draw_text("Premi ER tasto INVIO per iniziare", 480, 250,
                         arcade.color.PURPLE_HEART, font_size=20, anchor_x="center")
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RETURN:
            from gameview import GameView
            game_view = GameView()
            self.window.show_view(game_view)