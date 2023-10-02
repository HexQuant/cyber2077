from pynput import mouse, keyboard

aim_toggle = False
hack_toggle = False

# aim
ingame_aim_button = 'k'
trigger_aim_button = mouse.Button.right

# shift
ingame_dash_button = 'p'
ingame_run_button = keyboard.Key.shift_l
trigger_run_button = keyboard.Key.shift_l

# hack
ingame_hack_button = keyboard.Key.ctrl_l
trigger_hack_button = keyboard.Key.ctrl_l

keyb = keyboard.Controller()


def on_click(x, y, button, pressed):
    global aim_toggle
    if pressed and button == trigger_aim_button:
        if aim_toggle:
            keyb.release(ingame_aim_button)
            aim_toggle = False
        else:
            keyb.press(ingame_aim_button)
            aim_toggle = True
    return True


def on_scroll(x, y, dx, dy):
    global hack_toggle
    if hack_toggle:
        keyb.tap(ingame_hack_button)


def on_press(key):
    if key == trigger_run_button:
        keyb.tap(ingame_dash_button)
    if key == trigger_hack_button:
        global hack_toggle
        hack_toggle = True
    return True


def on_release(key):
    if key == trigger_hack_button:
        global hack_toggle
        hack_toggle = False
    return True


listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

with mouse.Listener(
        on_click=on_click,
        on_scroll=on_scroll,
) as listener:
    listener.join()
