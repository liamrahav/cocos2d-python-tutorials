# Alright!
# It's time for us to string everything we learned in the basics tutorial together

# Let's start with all of the inputs we need
import cocos
from cocos import scene
from cocos.layer import Layer, ColorLayer
from cocos.director import director
from cocos.scenes import *
from cocos.sprite import Sprite
from cocos.actions import *
from cocos.audio.pygame.mixer import Sound
from cocos.audio.pygame import mixer
from pyglet.window.key import symbol_string


# Here is how we will structure our code
# First, we will write an Audio class that is the child of SDL's Sound class
# Second we will write an Input layer that controls both the sprite and the audio
# And to spice things up, we'll add two states to the first layer: a normal and a trippy mode

# We start with the audio class, same as before
class Audio(Sound):
    def __init__(self, filename):
        super(Audio, self).__init__(filename)
        # Pretty easy, I'd say


# Let's be fancy and make this a color layer AND an event handler
class InputLayer(cocos.layer.ColorLayer):
    is_event_handler = True

    def __init__(self, x=320, y=240, is_trippy=False):
        super(InputLayer, self).__init__(46, 204, 113, 1000)

        # We set the trippy boolean based on the value passed in (by default it's not trippy)
        self.is_trippy = is_trippy

        # Now we need a little guy to manipulate
        self.sprite = Sprite('assets/img/grossini_dance_08.png')
        self.sprite.position = x, y
        self.sprite.opacity = 0
        self.add(self.sprite)
        self.sprite.do(FadeIn(2))

        # You should be bored seeing this same code over and over again
        # Here's something different though
        # Now I create an audio object and store it within self, based on whether or not it's trippy
        if self.is_trippy:
            # When it is trippy, I have a slowed down and distorted version of the song I made in Audacity
            self.bg_music = Audio("assets/sound/LatinIndustriesSlow.wav")
            # I also start running a couple effects that make it seem very trippy
            # It's important to note that you can do math on Cocos2D effects and actions
            self.do((Waves(duration=4) * 100) + Liquid(duration=15))
            # In this case I added two actions together and multiplied the waves by 100 for run
        else:
            # If it's not trippy then I just make it the same boring old song we've been using before
            self.bg_music = Audio("assets/sound/LatinIndustries.wav")

        # We lower the volume of the background music and have it play the whole time
        self.bg_music.set_volume(.2)
        self.bg_music.play(-1)

        # We don't need anything else here, let's just let our sprite be moved in the event handlers

    # So now we can overload some default event handlers
    # We'll let the user move in any direction on the screen with the arrow keys
    # We'll only be doing keyboard input for this program
    def on_key_press(self, key, modifiers):
        # If you don't know what these next couple lines do, go check the previous tutorials
        move_left = MoveBy((-50, 0), .5)
        move_up = MoveBy((0, 50), .5)

        # Check if they want to go left, and then actually make the sprite go left
        if symbol_string(key) == "LEFT":
            self.sprite.do(move_left)

        # Or maybe if they want to move right?
        elif symbol_string(key) == "RIGHT":
            self.sprite.do(Reverse(move_left))

        # Lastly we need to make it move up
        elif symbol_string(key) == "UP":
            self.sprite.do(move_up)

        # Oh yeah don't forget about down
        elif symbol_string(key) == "DOWN":
            self.sprite.do(Reverse(move_up))

        # That's it for movements!
        # Now let's look at transitioning to a new scene
        # Let's make the game all trippy when they hit space
        elif symbol_string(key) == "SPACE":
            # I need to stop the music before we transition to the next scene so that two songs aren't playing at once
            self.bg_music.stop()

            # If you were paying attention, you would've noticed I take three parameters in the init function
            # I get the X and Y coordinates of the sprite to figure out where to place it when the scenes transition
            coordinates = self.sprite.position
            # You should try printing the X and Y coordinates yourself to see the type of object that it returns
            if self.is_trippy:
                # This line only runs when the layer is already trippy, and by default the layer makes itself not trippy
                # This line only needs to give the X and Y coordinates in that case
                director.replace(scene.Scene(InputLayer(coordinates[0], coordinates[1])))
            else:
                # This huge line makes a new scene, with a transition, and inputs the coordinates and makes it trippy!
                director.replace(scene.Scene(InputLayer(coordinates[0], coordinates[1], True)))


# And finally we do our usual initialization and run the scene
mixer.init()
director.init()
director.run(scene.Scene(InputLayer()))