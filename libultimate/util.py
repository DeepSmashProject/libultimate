import numpy as np
from mss import mss

def capture():
    with mss() as sct:
        monitor = sct.monitors[1]
        img = sct.grab(monitor)
        frame = np.array(img)
        frame = np.array(frame)[:, :, :3] # bgra2bgr
        frame = frame[:,:,::-1].tolist()  # bgr2rgb
        return frame