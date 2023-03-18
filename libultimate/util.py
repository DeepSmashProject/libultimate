import numpy as np
from mss import mss
import base64

def capture():
    with mss() as sct:
        monitor = sct.monitors[0]
        img = sct.grab(monitor)
        frame = np.array(img)[:, :, :3].astype(np.uint8) # rgba2rgb
        return frame
    
def encode_image(image: np.array):
    return base64.b64encode(image.tobytes())

def decode_image(image_str: str, image_size: tuple):
    return np.frombuffer(base64.b64decode(image_str), dtype=np.uint8).reshape(image_size[0], image_size[1], 3)