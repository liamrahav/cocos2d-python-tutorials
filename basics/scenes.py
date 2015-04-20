# I won't explain the inputs this time - I think you guys are getting the jist of it
import cocos
from cocos.scene import Scene
from cocos.layer import Layer, ColorLayer
from cocos.director import director
from cocos.sprite import Sprite
from cocos.text import Label
from cocos.actions import *
from cocos.audio.pygame.mixer import Sound
from cocos.audio.pygame import mixer


# For this tutorial, we will be making two scenes and switching between them
# Theoretically, we could have two scenes made of the same layer, but there would be no visual difference between them
# For that reason we need to make two scenes with different text
# As a bonus I make them different colours as well


class Layer1(ColorLayer):
    # I set the layer to be an event handler because I want to be able to transition to another scene on a key press
    is_event_handler = True

    def __init__(self):
        # Remember that I need to pass in an RGBA colour value because it's a ColorLayer
        super(Layer1, self).__init__(155, 89, 182, 1000)

        # I make a simple label with no extra parameters such as font or anchors
        text = Label("This is the first scene")

        # For the position, I do something we haven't done before
        # We've been making the position static, but we don't exactly know the width and height of a player's window
        # Therefore, getting the virtual height and width and then just dividing them by two is a safer bet
        text.position = director._window_virtual_width / 2, director._window_virtual_height / 2

        # And lastly we add it
        self.add(text)

    # Here is the overload for the on_key_press function
    def on_key_press(self, key, modifiers):
        # Here is entire purpose of this lesson!
        director.replace(Scene(Layer2()))
        # That line replaces whatever scene is currently running in the director with the scene indicated
        # In this case, we create a new scene object inline out of the second layer, which I have coded below


# Here is the second Layer I make, for the second scene
class Layer2(ColorLayer):
    # Same as before, we let it handle user input
    is_event_handler = True

    # Initialize it and call the super class, but this time pass in a different colour
    def __init__(self):
        super(Layer2, self).__init__(231, 76, 60, 1000)

        # Same Label code as before but this time with different text
        text = Label("This is the second scene")
        text.position = director._window_virtual_width / 2, director._window_virtual_height / 2
        self.add(text)

    # And once again the same user input code
    def on_key_press(self, key, modifiers):
        director.replace(Scene(Layer1()))


# Here we initialize the director and start running the first scene
director.init()
director.run(Scene(Layer1()))

# But if you remember, when you press a key that layer will tell the director to make a new scene out of the second layer
# And that's about it. As you can see, it's pretty easy to switch between scenes