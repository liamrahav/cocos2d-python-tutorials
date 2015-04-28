# Imports as usual
from cocos.sprite import Sprite
from cocos.tiles import load
from cocos.layer import ScrollingManager, ScrollableLayer
from cocos.director import director
from cocos.scene import Scene
from cocos.actions import Driver
from pyglet.window import key

# Let's make a simple game where you drive around a track in a car
# This code is a simplified version of the one that exists in the cocos examples

# The first thing I need to do is initialize the director, because many other objects in this program depend on it
# This time I'm going to pass in a few more parameters than usual into the initialize function
director.init(width=800, height=600, autoscale=False, resizable=True)
# I simply set an X and Y for the window, and allow it to be resized

# Here I set a scroller and a key manager
# The key manager is something new you haven't seen!
# It allows me to get the keys being pressed, globally. Pretty neat!
keyboard = key.KeyStateHandler()

# And the scrolling manager like you saw last time
scroller = ScrollingManager()


# Here's something you haven't scene before!
# We'll be using the Driver class from the "move_actions" provided by Cocos, and editing it slightly for our needs
# The driver class is built to help make having sprites behave like vehicles much simpler
class CarDriver (Driver):
    # We don't need to call the init function because the Driver class already does that for us!

    # Instead I only want to overload this step function. This is what controls the movement of the sprite
    def step(self, dt):
        # This line might seem pretty complicated, but it's really not at all
        self.target.rotation += (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 100 * dt
        # Essentially what I do here is take the right value minus the left value (remember that moving left is negative)
        # And then I multiply it by 100 so it's more visible, and multiply it by the dt value passed in by the step function
        # Finally, I add it to the rotation of the "target", which would be the sprite we tell to do this action

        # Now I'm going to do something very similar for the sprite's acceleration
        self.target.acceleration = (keyboard[key.UP] - keyboard[key.DOWN]) * 350
        # See if you can figure this out yourself!

        # Next I'm going to make the car stop completely if the space key is held
        if keyboard[key.SPACE]:
            self.target.speed = 0
            # Pretty easy, huh?

        # That's basically it!
        # Now we just need to call the original step function to let it do its magic
        super(CarDriver, self).step(dt)

        # Lastly, this line simply tells the ScrollingManager to set the center of the screen on the sprite
        scroller.set_focus(self.target.x, self.target.y)


# Now we need to make a layer for the car itself!
# Remember that the layer needs to be scrollable so that the car can move around the map
class CarLayer(ScrollableLayer):
    def __init__(self):
        super(CarLayer, self).__init__()

        # Here we simply make a new Sprite out of a car image I "borrowed" from cocos
        self.sprite = Sprite("assets/img/car.png")

        # We set the position (standard stuff)
        self.sprite.position = 200, 100

        # Oh no! Something new!
        # We set a maximum forward and backward speed for the car so that it doesn't fly off the map in an instant
        self.sprite.max_forward_speed = 200
        self.sprite.max_reverse_speed = -100

        # Then we add it
        self.add(self.sprite)

        # And lastly we make it do that CarDriver action we made earlier in this file (yes it was an action not a layer)
        self.sprite.do(CarDriver())

# Now to the code that actually runs this game!
# Here I make a layer out of that CarLayer we defined before
car_layer = CarLayer()

# Next I load the map of the racetrack just as I did in the last tutorial
map_layer = load("assets/road_map.tmx")["map0"]

# Then we add them to the ScrollingManager
scroller.add(map_layer)
scroller.add(car_layer)
# Order is important! If we added the car layer first, the map would go on top and you wouldn't see the car

# Then we make a scene out of the scroller (just like we did before)
scene = Scene(scroller)

# This line is a bit random here but...
# I also need to push the handlers from the window to the object from Pyglet
# If I don't, it won't be able to handle the Cocos2D keyboard input!
director.window.push_handlers(keyboard)

# And finally we run the scene
director.run(scene)

# Now our games are actually starting to seem like, well, games!


