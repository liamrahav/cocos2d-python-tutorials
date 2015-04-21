from cocos.director import director
from cocos.layer import ColorLayer
from cocos.scene import Scene
from cocos.scenes import FadeTransition, SplitColsTransition
from cocos.text import Label

# Here is all the same code we had before, but this time we will be adding transitions between the scenes
# I won't be explaining what I already explained last tutorial
class Layer1(ColorLayer):
    is_event_handler = True

    def __init__(self):
        super(Layer1, self).__init__(155, 89, 182, 1000)

        text = Label("This is the first scene")
        text.position = director._window_virtual_width / 2, director._window_virtual_height / 2
        self.add(text)

    def on_key_press(self, key, modifiers):
        # Adding transitions into your Scenes is pretty easy
        # All you need to do is put a transition in the replace method
        director.replace(FadeTransition(Scene(Layer2())))
        # This specific transition is a simple Fade that makes the screen fade to black and then fade to the next scene
        # There are many different scenes available for you to use
        # You can check them out here: http://python.cocos2d.org/doc/api/cocos.scenes.transitions.html


class Layer2(ColorLayer):
    is_event_handler = True

    def __init__(self):
        super(Layer2, self).__init__(231, 76, 60, 1000)

        text = Label("This is the second scene")
        text.position = director._window_virtual_width / 2, director._window_virtual_height / 2
        self.add(text)

    def on_key_press(self, key, modifiers):
        # This is extremely similar to the one above
        director.replace(SplitColsTransition(Scene(Layer1())))
        # Except this time, we are using a Split Columns transition
        # It make three bars out of the screen, of which the middle one goes up and the others go down
        # Then the bars come back, this time containing the next scene
        # It sounds odd written out, but it's a neat transition when you view it

director.init()
director.run(Scene(Layer1()))