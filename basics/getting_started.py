"""
I chose these import statements just to make my close look cleaner
For this to work you would just need to import cocos and then add the subdirectory after
Ex: self.label = Label(...) would be self.sprite = cocos.text.Label(...)
"""
import cocos
from cocos.text import Label
from cocos import scene
from cocos.layer import Layer
from cocos.director import director


# This code is an explained version of the Hello World example from the Cocos2D Python documentation
# We will be making a simple game that displays the text "Hello World!"

# First I create a class that extends the Layer class from the Cocos library.
# If you don't know what this is you should probably take an object oriented programming course first
class HelloWorld(Layer):
    # Each python class needs an __init__ function that is called when an object is instantiated
    def __init__(self):
        # First you need to initialize the parent class, Layer, which is why I called the super function in this case
        super(HelloWorld, self).__init__()
        # First I make a Cocos Label object to display the text.
        hello_world_label = Label(
            "Hello World!",  # The first thing the Label class requires is a piece of text to display
            font_name = "Times New Roman", # The next thing we need to input a font. Feel free to replace it with any font you like.
            font_size = 32,  # The third input I give is a font size for the text
            anchor_x = 'center',  # This input parameter tells cocos to anchor the text to the middle of the X axis
            anchor_y = 'center'  # Similar to the input above, this parameter tells cocos to anchor the text to the middle of the Y axis
        )

        # Now I need to give the text its position.
        hello_world_label.position = 320, 240

        # Lastly I need to add the label to the layer
        # self refers to the object, which in this case is the layer
        self.add(hello_world_label)


# From here the code is pretty typical for a Cocos2D application
# First I need to initialize the cocos director
# The director is the part of cocos that "directs" the scenes. Cocos is pretty partial to this type of film language
director.init()
# Lastly I run the scene. This line of code is pretty long compared to the others, so I'll explain what each part does
# To begin I call the director's run function, which allows it to run the scene by placing layers within
director.run(
    # Next I create a Scene object that allows me to string the layers together. In this case I only have 1 layer
    scene.Scene(
        # And lastly I create the layer that we made above inside of the new scene
        HelloWorld()
    )
)

# That's it! Run it and see what happens