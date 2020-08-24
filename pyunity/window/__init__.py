"""
pyunity.window
==============
A module used to load the window providers.

Windows
-------
The window is provided by one of three
providers: FreeGLUT, GLFW and Pygame.
When you first import PyUnity, it checks
to see if any of the three providers
work. The testing order is as above, so
Pygame is tested last.

To create your own provider, create a
class that has the following methods:

- `__init__`: initiate your window and
    check to see if it works.
- `start`: start the main loop in your
    window. The first parameter is
    ``update_func``, which is called
    when you want to do the OpenGL calls.

Check the source code of any of the window
providers for an example. If you have a
window provider, then please email it
to me at tankimarshal2@gmail.com.

"""

import os
import OpenGL.GLUT, glfw, pygame
from ..errors import *

def glutCheck():
    global OpenGL
    OpenGL.GLUT.glutInit()
    del OpenGL

def glfwCheck():
    global glfw
    if not glfw.init():
        raise Exception
    glfw.create_window(50, 50, "Test", None, None)
    glfw.terminate()
    del glfw

def pygameCheck():
    global pygame
    if pygame.init()[0] == 0:
        raise Exception
    del pygame

def LoadWindowProvider():
    
    winfo = [
        ("FreeGLUT", glutCheck),
        ("GLFW", glfwCheck),
        ("Pygame", pygameCheck),
    ]

    windowProvider = ""
    failed = False

    for name, checker in winfo:
        i = 0
        next = winfo[i + 1][0] if i < len(winfo) else None
        if os.environ["PYUNITY_DEBUG_MODE"] == "1":
            print("Trying", name, "as a window provider")
        try:
            checker()
            windowProvider = name
        except Exception as e:
            print(e)
            failed = bool(next)
            if not failed: print(name, "doesn't work, trying", next)
        
        if failed is None: raise PyUnityException("No window provider found")
        if windowProvider: break
        i += 1

    if os.environ["PYUNITY_DEBUG_MODE"] == "1":
        print(f"Using window provider {windowProvider}")

    if windowProvider == "FreeGLUT":
        from .glutWindow import Window as glutWindow
        return glutWindow
    if windowProvider == "GLFW":
        from .glfwWindow import Window as glfwWindow
        return glfwWindow
    if windowProvider == "Pygame":
        from .pygameWindow import Window as pygameWindow
        return pygameWindow