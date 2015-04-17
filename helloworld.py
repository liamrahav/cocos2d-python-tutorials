# Specific cocos imports
from cocos import text
from cocos.director import director
from cocos.layer import Layer, ColorLayer
from cocos.scene import Scene
from cocos.actions import *
# Broad cocos import
import cocos


class HelloWorld(Layer):
    def __init__(self):
        super(HelloWorld, self).__init__()

        label = text.Label('Hello World',
                           font_name='Helvetica',
                           font_size=32,
                           anchor_x='center',
                           anchor_y='center')

        label.position = 320, 240

        self.add(label)


director.init()

hello_layer = HelloWorld()

main_scene = Scene(hello_layer)

director.run(main_scene)