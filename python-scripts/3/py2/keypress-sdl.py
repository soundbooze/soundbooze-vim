import sys
import sdl2
import sdl2.ext

def run():

    sdl2.ext.init()
    window = sdl2.ext.Window("Key", size=(800, 600))
    window.show()
    running = True

    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            elif event.type == sdl2.SDL_KEYDOWN:
                if event.key.keysym.sym == 113:
                    running = False
                    break

        window.refresh()

    return 0

if __name__ == "__main__":
    sys.exit(run())
