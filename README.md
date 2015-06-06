# Cocos Python Tutorials
------------------------

This repository contains a bunch of useful tutorials for getting started with Cocos2D for Python!

To get started and run the examples, open up your terminal and type `git clone https://github.com/LiamRahav/Cocos-Python-Tutorials.git` (assuming you have git installed) in whichever directory you want this repository in. Or you can use the GitHub desktop app, or download this as a ZIP file and then decompress it on your machine. It's up to you.

You will need to install Cocos2D to write these games. From the Cocos2D Python programming guide -
>cocos2d is a framework for building 2D games, demos, and other graphical/interactive applications.

----------------------------------------------------------------------------

Cocos2D has a quite a few dependencies, and you need them all. To begin, make sure you have pip installed. 
You can check this by running `pip -V` in terminal. You should get a version name and a directory, such as 
`pip 6.1.1 from /usr/local/lib/python2.7/site-packages (python 2.7)`. 
If you don't have pip installed, check this site for instructions: https://pip.pypa.io/en/stable/installing.html

Once you have pip you will need to install the following dependencies. Only the first two are required, but the rest provide additional support (such as particles and audio) that may come in handy later: 

###Six
Six is a compatibility library that allows for code to be more easily transferable between python 2.x and 3.x

To install it, run either ```pip install six``` or `sudo pip install six` depending on whether you are using venv or not.

###Pyglet
Pyglet is a python library for writing graphics in python. Cocos2D is built on top of Pyglet (for the most part).

To install it, run either `pip install pyglet` or `sudo pip install pyglet` depending on whether you are using venv or not.

###NumPy
NumPy is a python package that deals with complex mathematics and scientific computing. You'll need this for particle support.

On Mac, installation is made easy thanks to Homebrew. If you don't have it installed, run `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
` in terminal. Then you can simply run `brew install numpy` and `brew install scipy` to make sure you have the full SciPy package.

On other operating systems such as Windows or Linux distributions, head to http://www.scipy.org/install.html for more information on how to install for your particular operating system.

###AVbin
AVbin is a package that provides some audio and the video support for Cocos2D Python.

Head to https://avbin.github.io/AVbin/Download.html to download the correct installer for your operating system.

###SDL
SDL is the framework that PyGame (another Python game library) relies on for audio support. Cocos uses it for its audio as well.

Head over to https://www.libsdl.org/download-1.2.php to download the base SDL library and then to https://www.libsdl.org/projects/SDL_mixer/release-1.2.html to download the Mixer library from SDL (which was what we will be using for audio support in our games)

----------------------------------------------------------------------------
Now that you're all set up you should be ready to install Cocos2D

###Cocos2D
This is the most essential library for these tutorials and examples. It's pretty similar to install like everything else here.

Simply head to your terminal and type in `pip install cocos` or `sudo pip install cocos` depending on whether you are using venv.

----------------------------------------------------------------------------

### Tutorial Structure

The code is grouped in folders by their difficulty level. Here is how it's mostly layed out:

    root directory/
        |
        | readme
        | --> difficulty/
            |
            | --> assets/
            | readme
            | examples


From here you should be ready to start reading through the samples and trying out the concepts yourself. I group the the code by difficulty level, so I recommend starting in the `basics` folder and working your way up.

It's important to note that `basics` does not mean Python basics! You should at least have a basic grasp on writing object oriented code before trying to jump into Cocos2D Python!

*_I highly recommend that you browse through the code and READMEs on GitHub, and only use the cloned repository to run the games_*

-------------------------------------------------------------

Cocos has also provided some pretty good basic documentation and video samples, but unfortunately it stops there. You can check those out here http://python.cocos2d.org/doc/programming_guide/index.html


I created this repository because I found the Cocos2D Python documentation to be extremely limited, especially in code samples, beyond the basic level. It is also relatively complex and hard to understand. I often found myself needing to look at the source code for explanations on how to use certain classes and features. 
If I had tried to teach myself Cocos half a year ago, when I was just getting familiar with basic-intermediate concepts in Python, I would have been hopelessly confused. These guides are aimed towards people in that level.
