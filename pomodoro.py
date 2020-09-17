import os
from pathlib import Path
from PIL import Image
import time
import tqdm

def run(every=45):
    """Pop up a picture every X minutes. every defaults to 45."""
    print(f"Scheduling refuel time for every {every} minutes.")
    seconds = every * 60
    pic = Path.joinpath(Path(__file__).parent, "pic.png")
    try:
        img = Image.open(pic)
        while(True):
            for i in tqdm.trange(seconds):
                time.sleep(1)
            print(f"Taking rest at {time.ctime()}")
            img.show()
    except:
        print("Have a good day!")
        img.close()
