# Same imports once again

import cocos
from cocos.text import Label
from cocos import scene
from cocos.layer import Layer
from cocos.director import director
from cocos.sprite import Sprite

# Except for this import. This import, from Pyglet (one of the dependencies of cocos), is to recognize keyboard codes
from pyglet.window.key import symbol_string


# Similar starting code to before with one exception
class KeyboardInput(Layer):
    # You need to tell cocos that your layer is for handling input!
    # This is key (no pun intended)!
    # If you don't include this you'll be scratching your head wondering why your game isn't accepting input
    is_event_handler = True

    def __init__(self):
        super(KeyboardInput, self).__init__()

        # Let's make a Label like we did in the HelloWorld sample to show the keys being pressed
        # We will write code to append the key being pressed further down in the file
        self.label = Label("Keys: ",
                      font_name = "Helvetica",
                      font_size = 32,
                      anchor_x = "center",
                      anchor_y = "center")
        self.label.position = 320, 240

        # Here I make a variable to store the keys being pressed
        # set() creates a new set object.
        # A set object is an object built into Python that stores things in, you guessed it, sets
        # You can call the add() and remove() methods to modify the contents of a set
        self.keys_being_pressed = set()

        # Next I run my update_text function that I write further down in the file
        self.update_text()

        # And lastly I add my label to the layer!
        self.add(self.label)

    # This is the function that updates the label
    def update_text(self):
        # Here I get the name of the key
        # This line requires a bit of explanation
        # Essentially, I look at the key being pressed (which I set in a function further down)
        # And I match it up to the appropriate symbol for that string
        # So if the "T" key and the left "Shift" key were being pressed, this line would recognize their respective code,
        # And it would set the variable to "T", "LSHIFT"
        key_names = [symbol_string(k) for k in self.keys_being_pressed]

        # This line sets the text to the indicated string, joining in the key names until there are no more keys indicated
        text_for_label = "Keys: " + ", ".join(key_names)

        # This code is a bit lengthy, but essentially I'm just accessing the text element from the Label object
        self.label.element.text = text_for_label

    # This function is once of the default Cocos functions. I overload it and add my own code
    # By default this function just passes, but I make it actually do stuff!
    def on_key_press(self, key, modifiers):
        # By stuff I mean updating the keys_being_pressed variable with the key being passed in through Cocos
        self.keys_being_pressed.add(key)
        # Then I simply run my update text method to make sure the string gets updated
        self.update_text()

    # This function is also a default Cocos function!
    # I have to remember to update both the keys currently pressed and the string when they release a key
    # You can try commenting this out to see what happens when you hit a key and let go without this piece of code
    def on_key_release(self, key, modifiers):
        # Same code as before, except I remove instead of add the key
        self.keys_being_pressed.remove(key)
        self.update_text()

# And then I use the same code you're used to seeing to run the layer
director.init()
director.run(scene.Scene(KeyboardInput()))



