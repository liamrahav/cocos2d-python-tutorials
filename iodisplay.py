import cocos
import pyglet
from cocos.director import director
from cocos.layer import Layer
from cocos.text import Label
from pyglet.window.key import symbol_string


# This class displays what keys and modifiers you are holding down
class KeyDisplay(Layer):
    # This is the parameter you must set for the layer to receive input
    is_event_handler = True

    def __init__(self):
        super(KeyDisplay, self).__init__()

        self.text = Label("",
                          x=100,
                          y=280)

        # This code keeps track of which keys are being pressed:
        self.keys_pressed = set()
        self.update_text()
        self.add(self.text)

    def update_text(self):
        key_names = [symbol_string(k) for k in self.keys_pressed]
        text = 'Keys: ' + ','.join(key_names)
        # Update the text in self.text
        self.text.element.text = text

    # The next few functions are event functions from cocos that get triggered when the event name occurs
    def on_key_press(self, key, modifiers):
        self.keys_pressed.add(key)
        self.update_text()

    def on_key_release(self, key, modifiers):
        self.keys_pressed.remove(key)
        self.update_text()


# This layer displays where your mouse is
class MouseDisplay(Layer):
    is_event_handler = True

    def __init__(self):
        super(MouseDisplay, self).__init__()

        self.pos_x = 100
        self.pos_y = 240
        self.flavour = Label('Click anywhere to move coordinates!',
                             font_size=15,
                             x=100,
                             y=100)
        self.text = Label('No mouse events yet',
                          font_size=18,
                          x=self.pos_x,
                          y=self.pos_y)
        self.add(self.text)
        self.add(self.flavour)

    def update_text(self, x, y):
        text = 'Mouse @ %d,%d' % (x, y)
        self.text.element.text = text
        self.text.element.x = self.pos_x
        self.text.element.y = self.pos_y

    # The following functions are event handlers provided by Cocos
    def on_mouse_motion(self, x, y, dx, dy):
        self.update_text(x, y)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.update_text(x, y)

    def on_mouse_press(self, x, y, buttons, modifiers):
        self.pos_x, self.pos_y = director.get_virtual_coordinates(x, y)
        self.update_text(x, y)


director.init(resizable=True)
# Run a scene with our event displayers:
director.run(cocos.scene.Scene(KeyDisplay(), MouseDisplay()))