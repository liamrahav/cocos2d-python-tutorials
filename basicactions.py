# Specific cocos imports
from cocos.actions import *
from cocos.layer import Layer, ColorLayer
from cocos.text import Label
from cocos.sprite import Sprite
from cocos.director import director
# Broad import
import cocos


class Hello(ColorLayer):
    def __init__(self):
        super(Hello, self).__init__(64, 64, 224, 225)

        label = cocos.text.Label('Hello, World!',
                                 font_name='Helvetica',
                                 font_size=32,
                                 anchor_x='center', anchor_y='center')

        # Set the label to the center of the screen
        label.position = 320, 240
        self.add(label)

        # Create a sprite
        sprite = Sprite('assets/img/grossini_dance_08.png')
        sprite.position = 320, 240

        # Set animations
        sprite.scale = 3

        # Add self and animation
        self.add(sprite, z=1)
        scale = ScaleBy(3, duration=2)
        label.do(Repeat(scale + Reverse(scale)))
        sprite.do(Repeat(Reverse(scale) + scale))


director.init()
hello_layer = Hello()
hello_layer.do(RotateBy(360, duration=10))

main_scene = cocos.scene.Scene(hello_layer)
director.run(main_scene)