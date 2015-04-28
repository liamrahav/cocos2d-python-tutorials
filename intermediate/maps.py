# Imports as usual
from cocos.tiles import load
from cocos.layer import ScrollingManager
from cocos.director import director
from cocos.scene import Scene


# This code might seem odd as there are no classes or functions or anything...
# That's because when we load a map, it generates that Layer for us

# We start off by initializing the director. This is important, as we need the director for the rest of the code to work
director.init()

# Next we load the map, and we specifically state what layer of the map we want to load
MapLayer = load("assets/mapmaking.tmx")["map0"]
# If you want to, check the mapmaking.tmx file in the assets folder to see where I declare map0
# Otherwise, make sure you name the map properly in Tiled and refer to that name in the brackets after the load function

# Here is something new! I make a ScrollingManager object to contain my map layer
scroller = ScrollingManager()
# What the ScrollingManager does is, you guessed it, manage scrolling from us
# Cocos spares us the pain of having to deal with adding support for the map scrolling when you move to the sides of it

# From here we simply add the MapLayer we made out of the map to the ScrollingManager
scroller.add(MapLayer)

# And then we make a scene out of the ScrollingManager and run it in the director!
director.run(Scene(scroller))

# I highly recommend you try making an easy program like this with your own map
# It is very easy to mess up this code, as Cocos doesn't provide a lot of leeway
# Putting the code in the wrong order, not declaring the name of the map, not intializing the director, etc all break this program