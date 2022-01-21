
import os
from pynput.keyboard import Key, Listener
from win32gui import GetWindowText, GetForegroundWindow
current_window = (GetWindowText(GetForegroundWindow()))
os.system("title Test")
os.system("color") #137,142,255
items = {0: "", 1: "", 2:""}
index = 0
Clear = lambda: os.system("cls")

def Colour(hex, data):
    if hex == "898eff":
        return (f"\033[38;2;137;142;255m{data}")
    else:
        return (f"\033[38;2;255;255;255m{data}")
    pass


def Menu():
    match index:
        case 0:
            print(Colour("898eff", """  *                        o              +                 *                 .
       O                     .              .                      .                   *
               .                ██╗     ██╗   ██╗███╗  ██╗ █████╗    .-.,='``'=. +            |
 .                     *        ██║     ██║   ██║████╗ ██║██╔══██╗   `=/_       \           - o -
                                ██║     ██║   ██║██╔██╗██║███████║    |  '=._    |      .     |
            |              +    ██║     ██║   ██║██║╚████║██╔══██║  *  \     `=./`,
    *     - o -                 ███████╗╚██████╔╝██║ ╚███║██║  ██║      `=.__.=` `=`             O
            |        .          ╚══════╝ ╚═════╝ ╚═╝  ╚══╝╚═╝  ╚═╝             *
                              .                      o                    .                  +"""))


            print(Colour("", "                                    >>  ") + Colour("898eff", "Log into an account") + Colour("", "  <<") +Colour("", "\n                                   Register an account with Luna") + Colour("", "\n                                      Join our discord server") + Colour("", "\n                                               Exit"))
        case 1:
            print(Colour("898eff", """  *                        o              +                 *                 .
       O                     .              .                      .                   *
               .                ██╗     ██╗   ██╗███╗  ██╗ █████╗    .-.,='``'=. +            |
 .                     *        ██║     ██║   ██║████╗ ██║██╔══██╗   `=/_       \           - o -
                                ██║     ██║   ██║██╔██╗██║███████║    |  '=._    |      .     |
            |              +    ██║     ██║   ██║██║╚████║██╔══██║  *  \     `=./`,
    *     - o -                 ███████╗╚██████╔╝██║ ╚███║██║  ██║      `=.__.=` `=`             O
            |        .          ╚══════╝ ╚═════╝ ╚═╝  ╚══╝╚═╝  ╚═╝             *
                              .                      o                    .                  +"""))


            print(Colour("", "                                        Log into an account") + Colour("", "\n                               >>  ") + Colour("898eff", "Register an account with Luna") + Colour("", "  <<") + Colour("", "\n                                      Join our discord server") + Colour("", "\n                                               Exit"))
            pass
        case 2:
            print(Colour("898eff", """  *                        o              +                 *                 .
       O                     .              .                      .                   *
               .                ██╗     ██╗   ██╗███╗  ██╗ █████╗    .-.,='``'=. +            |
 .                     *        ██║     ██║   ██║████╗ ██║██╔══██╗   `=/_       \           - o -
                                ██║     ██║   ██║██╔██╗██║███████║    |  '=._    |      .     |
            |              +    ██║     ██║   ██║██║╚████║██╔══██║  *  \     `=./`,
    *     - o -                 ███████╗╚██████╔╝██║ ╚███║██║  ██║      `=.__.=` `=`             O
            |        .          ╚══════╝ ╚═════╝ ╚═╝  ╚══╝╚═╝  ╚═╝             *
                              .                      o                    .                  +"""))


            print(Colour("", "                                        Log into an account") +Colour("", "\n                                   Register an account with Luna") + Colour("", "\n                                  >>  ") + Colour("898eff", "Join our discord server") + Colour("", "  <<") + Colour("", "\n                                               Exit"))
            pass
        case 3:
            print(Colour("898eff", """  *                        o              +                 *                 .
       O                     .              .                      .                   *
               .                ██╗     ██╗   ██╗███╗  ██╗ █████╗    .-.,='``'=. +            |
 .                     *        ██║     ██║   ██║████╗ ██║██╔══██╗   `=/_       \           - o -
                                ██║     ██║   ██║██╔██╗██║███████║    |  '=._    |      .     |
            |              +    ██║     ██║   ██║██║╚████║██╔══██║  *  \     `=./`,
    *     - o -                 ███████╗╚██████╔╝██║ ╚███║██║  ██║      `=.__.=` `=`             O
            |        .          ╚══════╝ ╚═════╝ ╚═╝  ╚══╝╚═╝  ╚═╝             *
                              .                      o                    .                  +"""))


            print(Colour("", "                                        Log into an account") +Colour("", "\n                                   Register an account with Luna") + Colour("", "\n                                      Join our discord server") + Colour("", "\n                                           >>  ") + Colour("898eff", "Exit") + Colour("", "  <<"))
            pass
    pass

def on_press(key):
    pass

def on_release(key):
    global index
    if key == Key.up and index > 0:
        index -= 1
        Clear()
        Menu()
    elif key == Key.down and index < 3:
        index += 1
        Clear()
        Menu()
Menu()
while True:
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


