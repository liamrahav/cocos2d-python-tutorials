# Same inputs as keyboard except I also input the actions package from cocos
import cocos
from cocos.text import Label
from cocos import scene
from cocos.layer import Layer
from cocos.actions import *
from cocos.director import director
from cocos.sprite import Sprite
from pyglet.window.key import symbol_string

# Here we will be applying input to what we learned before by making our sprite perform these actions
# 1. Jump on a left click
# 2. Move left when the "LEFT" key is pressed
# 2. Move right when the "RIGHT" key is pressed


# Same starting code as usual
class InputExample(Layer):
    is_event_handler = True

    def __init__(self):
        super(InputExample, self).__init__()

        # Let's create a sprite this time instead of using Labels
        self.sprite = Sprite("assets/img/grossini_dance_08.png")
        self.sprite.position = 320, 240

        # While we're at it let's make it fancy by having our sprite fade in
        self.sprite.opacity = 0
        self.add(self.sprite)
        self.sprite.do(FadeIn(2))

        # Remember that our layer is an event handler
        # This means that I don't need to add any calls to functions to execute the actions on those events

    # Let's start with that jump action
    # To start I need to overload the default click function
    def on_mouse_press(self, x, y, buttons, modifiers):
        # Remember that we said we only wanted to jump on left clicks
        # The number 1 represents left clicks in Cocos
        # You can test this by adding a print statement for the buttons input
        if buttons == 1:
            # The Jump action requires 4 inputs
            # 1. How high on the Y axis the sprite should jump
            # 2. How far on the X axis the sprite should jump to
            # 3. How many times the sprite should jump
            # 4. How many seconds it should take for the action to complete
            self.sprite.do(Jump(50, 0, 1, 1))

            # Pretty easy, huh? Now let's do the movement

    # Once again we overload a default event handler
    def on_key_press(self, key, modifiers):
        # First I create a move actions because we programmers are lazy and hate having to retype code!
        move_left = MoveBy((-50, 0), .5)

        # Here's where that Pyglet symbol_string() function comes in handy
        # Rather than having to interpret an inconsistent code, I can simply interpret the word LEFT and RIGHT
        if symbol_string(key) == "LEFT":
            self.sprite.do(move_left)

        # Now I need to tell the layer what to do if the user inputs RIGHT
        if symbol_string(key) == "RIGHT":
            # This is a pretty awesome feature built into Cocos
            # I only wrote code for moving left, but I can use the Reverse() function instead of rewriting code
            # Reverse() simply tells Cocos to do the reverse action of whatever you pass into it.
            self.sprite.do(Reverse(move_left))
            

# And once again the same init code
director.init()
director.run(scene.Scene(InputExample()))