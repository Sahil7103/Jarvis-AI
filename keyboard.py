from pynput.keyboard import Key,Controller
from time import sleep

keyboard=Controller()

def volumeup():
    for i in range(20):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.2)

def volumedown():
     for i in range(20):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.2)
