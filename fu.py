import time, random 
import keyboard as keys
from pynput.keyboard import Key, Controller
from rich import print, pretty
from rich.progress import track

start_key = '.'

pretty.install()

try:
    print("[bright yellow]Oodlekode'[/]s personal [bright white]AntiAFK[/] LEGO Fortnite Idle Bot")
    print("Focus the LEGO Fortnite window and press [red]%s[/] to start the bot." % start_key)

    keyboard = Controller()
    while True:
        if keys.is_pressed(start_key):
            print("\n[bright yellow]Starting bot...[/] Close the window to stop the bot.")

            keys = ["w", "a", "s", "d"]

            while True:
                delay = random.randint(200,10000)
                msg = "      SLEEP %0.3f SECONDS " % (delay/1000.)
                for i in track(range(int(delay/100)), msg):
                    time.sleep(0.1)
                key = random.choice(keys)
                delay = random.randint(150,5500)
                msg = "PRESS %c FOR %0.3f SECONDS " % (key, delay/1000.)
                keyboard.press(key)
                for i in track(range(int(delay/100)), msg):
                    time.sleep(0.1)
                keyboard.release(key)
        else:
            time.sleep(0.1)
except SystemExit:
    pass
except KeyboardInterrupt:
    sys.exit()
    
