# Alright!
# It's time for us to string everything we learned in the basics tutorial together

# Let's start with all of the inputs we need
import cocos
from cocos import scene
from cocos.layer import Layer
from cocos.director import director
from cocos.sprite import Sprite
from cocos.actions import *
from cocos.audio.pygame.mixer import Sound
from cocos.audio.pygame import mixer
from pyglet.window.key import symbol_string


# Here is how we will structure our code
# First, we will write an Audio class that is the child of SDL's Sound class
# Lastly we will write an Input layer that controls both the sprite and the audio

# We start with the audio class, same as before
class Audio(Sound):
    def __init__(self, filename):
        super(Audio, self).__init__(filename)
        # Pretty easy, I'd say


# Let's be fancy and make this a color layer AND an event handler
class InputLayer(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self):
        super(InputLayer, self).__init__(46, 204, 113, 1000)

        # Now we need a little guy to manipulate
        self.sprite = Sprite('assets/img/grossini_dance_08.png')
        self.sprite.position = 320, 240
        self.sprite.opacity = 0
        self.add(self.sprite)
        self.sprite.do(FadeIn(2))

        # You should be bored seeing this same code over and over again
        # Here's something different though
        # Now I create a couple audio objects and store them within self
        self.jump_sound = Audio("assets/sound/bounce.wav")
        self.bg_music = Audio("assets/sound/LatinIndustries.wav")
        # We lower the volume of the background music and have it play the whole time
        self.bg_music.set_volume(.2)
        self.bg_music.play(-1)

        # We don't need anything else here, let's just let our sprite be moved in the event handlers

    # So now we can overload some default event handlers
    # We'll let the user move in any direction on the screen with the arrow keys, and jump around with the spacebar
    # We'll only be doing keyboard input for this program
    def on_key_press(self, key, modifiers):
        # If you don't know what these next couple lines do, go check the previous tutorials
        move_left = MoveBy((-50, 0), .5)
        move_up = MoveBy((0, 50), .5)
        jump = Jump(50, 0, 1, .25)

        # Check if they want to go left, and then actually make the sprite go left
        if symbol_string(key) == "LEFT":
            self.sprite.do(move_left)

        # Or maybe if they want to move right?
        elif symbol_string(key) == "RIGHT":
            self.sprite.do(Reverse(move_left))

        # And lastly we need that jump game to be strong
        elif symbol_string(key) == "UP":
            self.sprite.do(move_up)

        elif symbol_string(key) == "DOWN":
            self.sprite.do(Reverse(move_up))

        elif symbol_string(key) == "SPACE":
            self.sprite.do(jump)


# And finally we do our usual initialization and run the scene
mixer.init()
director.init()
director.run(scene.Scene(InputLayer()))