import numpy as np
from mss import mss

def capture():
    with mss() as sct:
        monitor = sct.monitors[0]
        img = sct.grab(monitor)
        frame = np.array(img)[:, :, :3].astype(np.uint8) # rgba2rgb
        return frame