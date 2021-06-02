import arcade
import pathlib

SCREEN_WIDTH= 1000
SCREEN_HEIGHT= 650

SCREEN_TITLE= "Arcade Platformer"

ASSETS_PATH =pathlib.Path(__file__).resolve().parent.parent


class Platformer(arcad.Window):
    def __init__(self) -> None:
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT,SCREEN_TITLE)

        self.coins= None
        self.background= None
        self.walls= None
        self.ladders= None
        self.goals= None
        self.enemies= None

        self.player= None

        self.physics_engine = None

        self.score = 0

        self.level = 1

        self.coin_sound = arcade.load_sound(
            stre(ASSETS_PATH/ "sounds" / "coin.wav")
        )

        self.jump_sound = arcade.load_sound(
            str(ASSETS_PATH / "sound" / "jump.wav")
        )

        self.victory_sound = arcade.load_sound(
            str(ASSETS_PATH / "sounds" / "victory.wav")
        )
        pass

    def setup(self):
        #sets up the game fpr the current level
        pass

    def on_key_press(self, key: int, modifiers: int):
        #process key presses
        #Arguments: key{int} -- wich key was pressed
        #modifiers{int} -- wocj modifiers were down

    def on_key_release(self, key. int, modifiers:int):
        """Processes key releases

       Arguments:
          key {int} -- Which key was released
            modifiers {int} -- Which modifiers were down at the time
      """

    def on_update(self,delta_time: float):
        """Updates the position of all game objects

        Arguments:
            delta_time {float} -- How much time since the last call
        """
        pass

    def on_draw(self):
        pass

    if __name__ == "__main__":
        window = Platformer()
        window.setup()
        arcade.run()