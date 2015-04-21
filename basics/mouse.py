# Same imports once again, no pyglet keyboard input this time

import cocos
from cocos.text import Label
from cocos import scene
from cocos.layer import Layer
from cocos.director import director
from cocos.sprite import Sprite


# I make the layer, set it to an event handler, and initialize the super class to begin
class MouseInput(Layer):
    is_event_handler = True

    def __init__(self):
        super(MouseInput, self).__init__()

        # This time I set variables for the position rather than hardcoding it
        # I do this because we will want to alter these values later
        self.position_x = 100
        self.position_y = 240

        # Once again I make a label
        self.text = Label("No mouse interaction yet",
                          font_name = "Helvetica",
                          font_size = 24,
                          x = self.position_x,
                          y = self.position_y)

        # Then I just add the text!
        self.add(self.text)

    # Like last time we need to make a function to update that self.text label to display the mouse data
    def update_text(self, mouse_x_pos, mouse_y_pos):
        # I make a text variable and store a string containing the x and y positions passed into the function
        text = 'Mouse is at %d,%d' % (mouse_x_pos, mouse_y_pos)

        # Next I simply do what I did for the keyboard and update the self.text label to contain our new string
        self.text.element.text = text

        # I also update its now dynamic position by moving the text to wherever the user clicks
        self.text.element.x, self.text.element.y = self.position_x, self.position_y

    # Also similarly to the keyboard, I overload a few default functions that do nothing
    # I make all of them update the text, and I make clicks update both the text and the label's position
    def on_mouse_motion(self, x, y, dx, dy):
        self.update_text(x, y)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.update_text(x, y)

    def on_mouse_press(self, x, y, buttons, modifiers):
        # This next line seems a bit odd, and that's because it is!
        self.position_x, self.position_y = director.get_virtual_coordinates(x, y)
        # It introduces a new topic, virtual coordinates
        # If I had used default coordinates, the position might be updated in the OS's coordinates rather than the scene
        # The director provides us with the appropriate coordinates within our "virtual" window

        self.update_text(x, y)

# Just your standard stuff down here
director.init()
director.run(scene.Scene(MouseInput()))