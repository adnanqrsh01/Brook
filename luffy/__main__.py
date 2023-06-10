import glob
from pathlib import Path
import logging
from . import bot


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

path = "luffy/plugins/*.py"
files = glob.glob(path)

for name in files:
    with open(name) as a:
        pxt = Path(a.name)
        plugs = pxt.stem
        # Do whatever you need with 'plugs' variable here
        print(f"Loaded plugin: {plugs}")

print("luffy BOT STARTED & LOADED ALL PLUGINS")

if __name__ == "__main__":
    bot.run_until_disconnected()
