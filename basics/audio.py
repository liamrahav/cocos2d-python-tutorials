# Again very similar inputs to what we had before
from cocos import scene
from cocos.layer import Layer
from cocos.director import director

# Except for these imports
# It might seem odd that it's importing from pygame, but really it's importing SDL libraries
from cocos.audio.pygame.mixer import Sound
from cocos.audio.pygame import mixer


# Our first multi-class program! Nice
# First we need to create a wrapper around the SDL Sound class
# We do this by creating our own object that simply initializes the parent with a file name that we pass in
# You'll see this in action in a second
class Audio(Sound):
    def __init__(self, audio_file):
        # As stated above, we initialize the super class with the audio file we passed in
        super(Audio, self).__init__(audio_file)


# Here we create your standard layer
class AudioLayer(Layer):
    def __init__(self):
        super(AudioLayer, self).__init__()
        # Now, in the layer we create an Audio object from the class we described above
        song = Audio("assets/sound/LatinIndustries.ogg")
        # And lastly we make the song play when the layer is initialized
        song.play(-1)  # Setting the parameter to -1 makes the song play indefinitely


# Now we have more things to initialize than just the director
director.init()
# The audio mixer also needs us to tell it to get ready!
mixer.init()

# And lastly we run the scene like usual
director.run(scene.Scene(AudioLayer()))
