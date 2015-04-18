
# I chose these import statements just to make my code look cleaner
# For this to work you would just need to import cocos and then add the subdirectory after
# Ex: self.sprite = Sprite('directory') would be self.sprite = cocos.sprite.Sprite('directory')
import cocos
from cocos.layer import Layer, ColorLayer
from cocos import layer
from cocos.sprite import Sprite
from cocos.actions import *
from cocos.director import director
from time import sleep


# Here I make a class that extends cocos' ColorLayer class
# This type of layer is different because it has a background color! (awesome right?)
class Actions(ColorLayer):
    # When I initialize it I need to pass in an RRGB colour value so it can set the ColorLayer's background
    # I grabbed the Peter River colour (#3498db) from http://flatuicolors.com for this sample
    def __init__(self):
        super(Actions, self).__init__(52, 52, 152, 219)

        # I initialize a sprite using the cocos sprite.Sprite class
        # Change the path below to whatever your sprite image is
        self.sprite = Sprite('assets/img/grossini_dance_08.png')

        # I set the sprite's position to the center of the screen
        self.sprite.position = 320, 240

        # Here are all the actions I make my sprite perform
        # Check those class functions for info on how to code them!
        self.fade_in()
        self.move_left()
        self.move_right()
        self.move_right()

    def fade_in(self):
        # First I make a FadeIn animation object
        fade_action = FadeIn(2)

        # I set the sprite opacity to 0 so that it doesn't flash on the screen.
        # You should try removing this to see what happens
        self.sprite.opacity = 0

        # I add the sprite to the screen (remember it can't be seen yet)
        self.add(self.sprite, z=1)

        # I then start the fading in (which takes 2 seconds)
        # I don't need to reset the opacity because the FadeIn action does that for me!
        self.sprite.do(fade_action)

    def move_left(self, sleep_time=2):
        # First I make a MoveBy animation object
        # I set this to move -150 on the X axis, 0 on the Y axis, and to take 2 seconds
        left = MoveBy((-150, 0), 2)

        # Finally I make my sprite move left
        self.sprite.do(left)

        # I need to make the program sleep so that it lets this animations finish
        sleep(sleep_time)

    def move_right(self, sleep_time=2):
        # If you notice, this method is exactly the same as the move left method, but it moves +150 instead of -150

        # First I make a MoveBy animation object
        # I set this to move +150 on the X axis, 0 on the Y axis, and to take 2 seconds
        right = MoveBy((150, 0), 2)

        # And I make my sprite move right (just like in left)
        self.sprite.do(right)

        # Again I need my program to sleep for the 2 seconds the animation requires
        sleep(sleep_time)


# I initialize the director and run the layer (this is typical for cocos programs)
director.init()
director.run(cocos.scene.Scene(Actions()))

