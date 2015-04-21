from cocos.director import director
from cocos.layer import ColorLayer
from cocos.scene import Scene
from cocos.sprite import Sprite
from pyglet.window.key import symbol_string
from cocos.actions import *


class EffectLayer(ColorLayer):
    is_event_handler = True

    def __init__(self):
        super(EffectLayer, self).__init__(231, 76, 60, 1000)

        sprite = Sprite("assets/img/grossini_dance_08.png")
        sprite.position = 320, 240
        self.add(sprite)

    def on_key_press(self, key, modifiers):
        if symbol_string(key) == "T":
            self.do(Twirl(amplitude=5, duration=2))

        elif symbol_string(key) == "W":
            self.do(Reverse(Waves(duration=2)))

        elif symbol_string(key) == "F":
            self.do(FlipX3D(duration=1) + FlipY3D(duration=1) + Reverse(FlipY3D(duration=1)))


director.init()
director.run(Scene(EffectLayer()))