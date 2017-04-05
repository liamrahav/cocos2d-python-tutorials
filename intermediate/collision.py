# Import statements as usual
from cocos.sprite import Sprite
from cocos.tiles import load
from cocos.mapcolliders import RectMapCollider
from cocos.layer import ScrollingManager, ScrollableLayer, ColorLayer
from cocos.director import director
from cocos.scene import Scene
from cocos.actions import Action
from pyglet.window import key


# For this scene, we'll be using a map with a high rectangular block that we don't want the player to be able to pass

# Just as before, I start by initializing the director
director.init(width=700, height=500, autoscale=False, resizable=True)
# This is because, as stated before, many other objects depend on the director being initialized

# And, one again, we set the keyboard and scrolling managers
scroller = ScrollingManager()
keyboard = key.KeyStateHandler()

# I'll also throw in the line that pushes Cocos's handlers to the keyboard object
director.window.push_handlers(keyboard)

# We'll also load the tilemap here for clarity, as I will be using it in the class below
map_layer = load("assets/platformer_map.xml")['map0']
# I use Cocos's XML spec for this map! Check it out if you want to see how to code your own Cocos style maps


# This time we'll make an action that extends both the Action class and the new RectMapCollider
# The RectMapCollider, you guessed it, lets us collide with rectmaps (A.K.A. tilemaps)
class GameAction(Action, RectMapCollider):
    # To begin, we'll add a function for when the Action starts
    # I use the start function instead of an __init__ function because of the way the Action parent class is structured
    def start(self):
        # We simply set the velocity of the target sprite to zero
        self.target.velocity = 0, 0

        # We also tell the game that our sprite is starting on the ground
        self.on_ground = True
    def on_bump_handler(self, vx, vy):
        return (vx, vy)

    # Now once again we update this "step" function
    def step(self, dt):
        # To begin we get the delta x and delta y values by grabbing the appropriate parts of the target's velocity
        dx = self.target.velocity[0]
        dy = self.target.velocity[1]

        # Now we make the delta x value equal to the amount left or right they are telling their sprite to move
        dx = (keyboard[key.RIGHT] - keyboard[key.LEFT]) * 250 * dt
        # This is almost the same as before - once again I combine the left and right values and amplify it so it's visible

        # Here I do the opposite of that "gravity" code I wrote before
        # If the player is on the ground and they hit space...
        if self.on_ground and keyboard[key.SPACE]:
            # they jump into the air the amount that the gravity pulls down
            dy = 1500

        # What we do here may seem a bit odd, but it essentially acts as gravity for the target
        dy -= 1500 * dt
        # I subtract a number, in this case I chose 1500, from the delta y to make it come back down to the floor of the map

        # Here is all of the code for the collision of the target
        # What we do is get a "bounding rectangle", or the imaginary box around the sprite, from the last frame
        last_rect = self.target.get_rect()

        # Then we copy it into a new bounding rectangle that we can alter the values of to match what our math has done
        new_rect = last_rect.copy()

        # So we simply add our new X value to the old one (if it's moving left it will subtract instead)
        new_rect.x += dx

        # And we add our new Y value to the old one as well!
        new_rect.y += dy * dt

        # Now we need to actually check for collisions
        self.target.velocity = self.collide_map(map_layer, last_rect, new_rect, dy, dx)
        # What this line does is run the collide_map function from RectMapCollider to figure out new dx and dy values
        # Then it sets the target's velocity equal to those new dx and dy values

        # Here we check if it is on the ground by looking at the previous bounding rect's y and the current one's y
        # If they're both the same, we know that the target has not moved off the ground!
        self.on_ground = bool(new_rect.y == last_rect.y)

        # Now we need to anchor the position of the target to the middle of the bounding rectangle (or else the target won't move)
        self.target.position = new_rect.center

        # And lastly we set the focus of the scroller to the center of the player (which is the center of the rect)
        scroller.set_focus(*new_rect.center) # The * sets the argument passed in as all of the required parameters


# Now, once again, we make another class for the sprite's layer
# Remember that it must be a ScrollableLayer
class SpriteLayer(ScrollableLayer):
    def __init__(self):
        super(SpriteLayer, self).__init__()

        # And, just like last time, we make our sprite and have it do the action we define
        self.sprite = Sprite("assets/img/grossini.png")
        self.add(self.sprite)
        self.sprite.do(GameAction())

# The first thing we do in our "main" code is make the layer we just defined
sprite_layer = SpriteLayer()

# Now here's some more code we haven't done before
# Essentially, we need to find the cell where I marked for the player to start, and set the sprite as starting there
# We do this by first finding that cell I marked (check the source code of the map to see how it's done)
start = map_layer.find_cells(player_start=True)[0]

# Then I get that bounded rectangle we talked about earlier from the sprite
rect = sprite_layer.sprite.get_rect()

# After that I set the middle bottom of the sprite's bounded rectangle equal to the middle bottom of the start cell
rect.midbottom = start.midbottom

# And lastly I set the position of the sprite to the center of the rectangle
sprite_layer.sprite.position = rect.center

# From here it's pretty easy sailing
# First I add the map, and set the "z" to 0
scroller.add(map_layer, z=0)
# The z is the vertical axis, so the highest z value layer will always show on top of the others

# Then I add the sprite, and set the z to 1 so that it shows on top of the map layer
scroller.add(sprite_layer, z=1)

# Then I make a ColorLayer, just to spice up the background a bit (which for now is just transparent)
bg_color = ColorLayer(52, 152, 219, 1000)

# Then I make a scene
scene = Scene()
# And I add the scroller to it and put it on top of the stack of layers
scene.add(scroller, z=1)

# And I add the background color (I don't need to define a z because by default it's 0)
scene.add(bg_color)

# And then we run it!
director.run(scene)

# Now our games are starting to get a bit more complex, but it's nothing you can't handle!
