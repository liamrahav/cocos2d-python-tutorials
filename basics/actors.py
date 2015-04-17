# Here we will have the same starting code as we did in the last tutorial, except with a few different imports

import cocos
from cocos.text import Label
from cocos import scene
from cocos.layer import Layer
from cocos.director import director
from cocos.sprite import Sprite


class Actors(Layer):
    def __init__(self):
        super(Actors, self).__init__()

        # Here is where the code starts to get different
        # Instead of text, I create a sprite object
        # Also unlike last time, I added the sprite to the object instead of making it local
        # This is useful if you want to access it in other functions, like I will show in the next tutorial
        self.actor = Sprite('assets/img/grossini_dance_08.png')

        # Then I add it to the layer, similar to the text
        self.actor.position = 320, 240

        # And lastly I add it to the layer. Standard stuff
        self.add(self.actor)

# Now I initialize the director and run the scene just like before
director.init()
director.run(scene.Scene(Actors()))