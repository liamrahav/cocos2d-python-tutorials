from cocos.audio.pygame import mixer
from cocos.audio.pygame.mixer import Sound
from cocos.director import director
from cocos.menu import Menu, CENTER, MenuItem, shake, shake_back
from cocos.scene import Scene
from pyglet.app import exit

# Here we will make a simple menu that allows you to play/pause a song, and to increase or decrease its volume
# As you'll see, Cocos makes writing menus EXTREMELY easy. Like I probably should have put this in beginner easy


# To begin, we have to make a wrapper for the Sound class (remember this?)
class Audio(Sound):
    def __init__(self, audio_file):
        super(Audio, self).__init__(audio_file)


# Now here's the new part
# We make a class that extends Cocos's Menu class
class AudioMenu(Menu):
    def __init__(self):
        # When we initialize the super class, we can to pass in a title for our awesome menu, that will be displayed above it
        super(AudioMenu, self).__init__("AUDIO CONTROL")
        # if you want to add your own, personalized text, feel free to pass nothing in

        # Then we simply set the vertical and horizontal alignment (in this case center for both)
        self.menu_valign = CENTER
        self.menu_halign = CENTER
        # The cocos.menu file comes with many more different positions you can mix and match to get what you like

        # Next we need to make our menu items
        # This is the important part!
        # What we do is create a list filled with MenuItem objects
        menu_items = [
            # Each MenuItem has text to display, and a callback method
            # The callback method we pass in gets called when a user clicks on the MenuItem
            (MenuItem("Play/Pause", self.play_music)),
            (MenuItem("Increase Volume", self.volume_up)),
            (MenuItem("Decrease Volume", self.volume_down)),
            (MenuItem("Exit", self.on_quit))
            # Pretty easy I'd say
        ]

        # Now let's set the song we want them to hear (good god I love me some Latin Industries)
        self.song = Audio("assets/sound/LatinIndustries.ogg")

        # Then we simply create the menu using the create_menu method and passing in our MenuItem list
        self.create_menu(menu_items)

        # And I set the is_playing status to False, which we will access for our Play/Pause functionality
        self.is_playing = False

    # So, if you were paying attention, you'd notice that this is the first callback method we passed into the list
    def play_music(self):
        # If it is playing, I stop the song and set the boolean to false
        if self.is_playing:
            self.song.stop()
            self.is_playing = False
        # If not, I need to play the song (indefinitely I might add), and then set the boolean value to true
        else:
            self.song.play(-1)
            self.is_playing = True

    # Now for the volume up functionality
    def volume_up(self):
        # First I grab the current volume of the song
        volume = self.song.get_volume()
        # Then I set the volume to that volume, but I add just a smidgen to it (remember that volume is from 0.0 - 1.0)
        self.song.set_volume(volume + .1)

    # And the exact opposite for volume down
    def volume_down(self):
        volume = self.song.get_volume()
        self.song.set_volume(volume - .1)

    # IMPORTANT!
    # All your menus must have this on_quit function or they will not exit even if you press escape
    # (That means some fun Control+Alt+Tabing for you Windows users)
    def on_quit(self):
        # It seems odd that I need a function that literally just calls the exit function but...
        exit()
        # You've gotta do what you've gotta do


# Then we initialize the mixer (I bet you forgot about this!)
mixer.init()
# And initialize the director like usual
director.init(resizable=True)
# Finally, we run the scene
director.run(Scene(AudioMenu()))

# ... Yep this definitely should have been in beginner