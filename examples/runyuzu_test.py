#from pynput.mouse import Button, Controller
from pynput import mouse, keyboard
import time
m = mouse.Controller()
k = keyboard.Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
    m.position))

########## First Yuzu Help Menu ##########
m.position = (776, 383) # First Yuzu Help Menu
print('Now we have moved it to {0}'.format(
    m.position))
m.press(mouse.Button.left)
m.release(mouse.Button.left)
time.sleep(1)

######## Install DLC File #########
# Set pointer position
m.position = (226, 125) # Files menu
print('Now we have moved it to {0}'.format(
    m.position))
m.press(mouse.Button.left)
m.release(mouse.Button.left)
time.sleep(0.1)
m.position = (226, 153) # Install Nand
m.press(mouse.Button.left)
m.release(mouse.Button.left)
time.sleep(1)

## Select Files
string = (
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Challenger Pack 11] [01006A800016F00C][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Super Smash Bros Ultimate Challenger Pack 10] [01006A800016F00B][v65536].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Super Smash Bros Ultimate Challenger Pack 1] [01006A800016F002][v65536].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Super Smash Bros Ultimate Challenger Pack 2] [01006A800016F003][v131072].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Super Smash Bros Ultimate Challenger Pack 3] [01006A800016F004][v131072].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Super Smash Bros Ultimate Challenger Pack 4] [01006A800016F005][v131072].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Super Smash Bros Ultimate Challenger Pack 5] [01006A800016F006][v131072].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Super Smash Bros Ultimate Challenger Pack 6] [01006A800016F007][v65536].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Super Smash Bros Ultimate Challenger Pack 7] [01006A800016F008][v65536].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Super Smash Bros Ultimate Challenger Pack 8] [01006A800016F009][v131072].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Super Smash Bros Ultimate Challenger Pack 9] [01006A800016F00A][v65536].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Super Smash Bros Ultimate Piranha Plant Standalone Fighter] [01006A800016F001][v65536].nsp" '
'"/workspace/games/SSBU/Super Smash Bros. Ultimate [01006A800016E800][v1703936].nsp" '
)
for s in string:
    k.press(s)
    k.release(s)

time.sleep(1)
m.position = (885, 495) # File Open Button
m.press(mouse.Button.left)
m.release(mouse.Button.left)
time.sleep(0.1)
m.press(mouse.Button.left)
m.release(mouse.Button.left)
time.sleep(1)
m.position = (938, 463) # Install Button
m.press(mouse.Button.left)
m.release(mouse.Button.left)
time.sleep(10) # Installing...
m.position = (676, 365) # Finished Install Button
m.press(mouse.Button.left)
m.release(mouse.Button.left)


######## Install NSP File  ##########

# Set pointer position
m.position = (226, 125) # Files menu
print('Now we have moved it to {0}'.format(
    m.position))
# Press and release
m.press(mouse.Button.left)
m.release(mouse.Button.left)
time.sleep(0.1)
m.position = (226, 185) # Load File
m.press(mouse.Button.left)
m.release(mouse.Button.left)
time.sleep(1)

# in File Select
string = "/workspace/games/SSBU/Super Smash Bros Ultimate [v0].nsp"
for s in string:
    k.press(s)
    k.release(s)

time.sleep(1)
m.position = (885, 495) # File Open Button
m.press(mouse.Button.left)
m.release(mouse.Button.left)
time.sleep(0.1)
m.press(mouse.Button.left)
m.release(mouse.Button.left)
time.sleep(1)
m.position = (711, 416) # Install Button
m.press(mouse.Button.left)
m.release(mouse.Button.left)
time.sleep(30) # Waiting Load App
########### Restart Once ###########

# Set pointer position
m.position = (287, 125) # Files menu
print('Now we have moved it to {0}'.format(
    m.position))
# Press and release
m.press(mouse.Button.left)
m.release(mouse.Button.left)
time.sleep(0.1)
m.position = (287, 224) # Load File
m.press(mouse.Button.left)
m.release(mouse.Button.left)
time.sleep(1)