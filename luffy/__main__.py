import glob
from pathlib import Path
import logging
from . import bot
from luffy.utils import load_plug
from sys import argv

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

path = "luffy/plugins/*.py"
files = glob.glob(path)

for name in files:
    with open(name) as a:
        pxt = Path(a.name)
        plugs = pxt.stem
        # Do whatever you need with 'plugs' variable here
        print(f"Loaded plugin: {plugs}")

        load_plug(plugs.replace(".py", ""))

if __name__ == "__main__":
  if len(argv) not in (1, 3, 4):
      bot.disconnect()

  else:
      bot.run_until_disconnected()
