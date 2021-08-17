try:
    import pyautogui
    from pynput import keyboard
    from pynput.keyboard import Key
except:
    print("Please Run 'setup.bat' before run this script")

#  ======== settings ========
delay = 0.04  # in seconds
resume_key = keyboard.Key.f3
pause_key = keyboard.Key.f4
exit_key = keyboard.Key.esc
#  ==========================

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// AutoClicker by DeltCrosX")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t F3 = Resume")
    print("\t F4 = Pause")
    print("\t Esc = Exit")
    print("-----------------------------------------------------")
    print('Press F3 to start ...')


def main():
    lis = keyboard.Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
    lis.stop()


if __name__ == "__main__":
    main()
