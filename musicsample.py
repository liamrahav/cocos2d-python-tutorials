from cocos.audio.pygame.mixer import *
from cocos.layer import Layer
import cocos
from cocos.director import director
from time import sleep
from cocos.scene import Scene


class AudioLayer(Layer):
    def __init__(self):
        super(AudioLayer, self).__init__()

        self.sound = Sound('assets/sound/sound.wav')
        self.channel = self.sound.play()
        sleep(2)
        # This plays at 90% (1 * .9)
        self.sound.set_volume(0.9)
        sleep(2)
        # This plays at 60% (1 * .6)
        self.sound.set_volume(0.6)
        sleep(2)
        # This plays at 30% (.5 * .6)
        self.channel.set_volume(0.5)

        # This is in milliseconds
        self.sound.fadeout(2000)

director.init()
director.run(Scene(AudioLayer()))