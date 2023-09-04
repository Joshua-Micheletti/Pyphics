import sys

import glfw

from utils.parsers import argument_parser as ap
from utils.timer.Timer import Timer
from window.Window import Window
from renderer.Renderer import Renderer

def main():
    ap.parse_arguments(sys.argv)

    window = Window()
    renderer = Renderer()

    frametime = Timer()
    print_timer = Timer()

    while not glfw.window_should_close(window.window):
        # renderer.render()
        
        glfw.swap_buffers(window.window)
        glfw.poll_events()

        if print_timer.elapsed() > 2000:
            frametime.elapsed(True, True)
            print_timer.reset()

        frametime.reset()
        

            

if __name__ == "__main__":
    main()