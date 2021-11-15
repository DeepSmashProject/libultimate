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

# in File Select
'''

'"/workspace/games/SSBU/Super Smash Bros Ultimate [Fighters Pass Bonus Mii Fighter Costume Ancient Soldier] [01006A800016F016][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 1 -Challenge various Spirits!-] [01006A800016F065][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 1 -Challenge various Spirits!-] [01006A800016F066][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 1 -Challenge various Spirits!-] [01006A800016F067][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 1 -Challenge various Spirits!-] [01006A800016F068][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 2 -Challenge Strong Enemies!-] [01006A800016F069][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 2 -Challenge Strong Enemies!-] [01006A800016F06A][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 2 -Challenge Strong Enemies!-] [01006A800016F06B][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 2 -Challenge Strong Enemies!-] [01006A800016F06C][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 2 -Challenge Strong Enemies!-] [01006A800016F06D][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 3 -Bonus 5000 in-game Gold and 3 Classic Tickets -] [01006A800016F06E][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 3 -Bonus 5000 in-game Gold and 3 Classic Tickets -] [01006A800016F06F][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 4 -Bolster Your Spirits-] [01006A800016F070][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 4 -Bolster Your Spirits-] [01006A800016F071][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 4 -Bolster Your Spirits-] [01006A800016F072][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 4 -Bolster Your Spirits-] [01006A800016F073][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 5 -Snipe your Target!-] [01006A800016F077][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 5 -Snipe your Target!-] [01006A800016F078][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 5 -Snipe your Target!-] [01006A800016F079][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 5 -Snipe your Target!-] [01006A800016F07A][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 5 -Snipe your Target!-] [01006A800016F07B][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 7 - Challenge Powerful Enemies! -] [01006A800016F07E][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 7 - Challenge Powerful Enemies! -] [01006A800016F07F][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 7 - Challenge Powerful Enemies! -] [01006A800016F080][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 7 - Challenge Powerful Enemies! -] [01006A800016F081][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Board Challenge Pack 7 - Challenge Powerful Enemies! -] [01006A800016F082][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Booster Bundle #2 - Reaching Lv MAX] [01006A800016F087][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirit Booster Bundle #2 - Reaching Lv MAX] [01006A800016F088][v0].nsp" '

'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Aerith_s Outfit] [01006A800016F045][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Akira Outfit and Wig] [01006A800016F031][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Alta'$'\303\257''r Outfit and Hood] [01006A800016F034][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Arthur_s Armor and Helm] [01006A800016F048][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Barret_s Outfit] [01006A800016F043][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Bomberman Outfit and Mask] [01006A800016F041][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Callie Outfit and Wig] [01006A800016F039][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Chocobo Hat] [01006A800016F046][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Creeper Outfit and Mask] [01006A800016F03D][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Cuphead Outfit and Hat] [01006A800016F033][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Dante Outfit and Wig] [01006A800016F04C][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Diamond Armor and Helmet] [01006A800016F03F][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Erdrick_s Armor and Helmet] [01006A800016F025][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Felyne Hat] [01006A800016F049][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Geno Hat + Outfit] [01006A800016F047][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Gil_s Armor and Helmet] [01006A800016F042][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Goemon Outfit and Wig] [01006A800016F02A][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Heihachi Outfit and Wig] [01006A800016F03C][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Hunter_s Mail and Helm] [01006A800016F04A][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Iori Yagami Outfit and Wig] [01006A800016F030][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Jacky_s Outfit and Wig] [01006A800016F032][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Knuckles Outfit and Hat] [01006A800016F024][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Marie Outfit and Wig] [01006A800016F03A][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Martial Artist Gi and Wig] [01006A800016F026][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''MegaMan EXE_s Armor and Helmet] [01006A800016F037][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Morgana Hat] [01006A800016F022][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Nakoruru Outfit and Wig] [01006A800016F02F][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Ninjara Outfit and Wig] [01006A800016F038][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Persona 3 Protagonist Outfit and Wig] [01006A800016F01F][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Persona 4 Protagonist Outfit and Wig] [01006A800016F020][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Pig Outfit and Mask] [01006A800016F03E][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Proto Man_s Armor and Helmet] [01006A800016F02C][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Rabbids Hat] [01006A800016F035][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Rathalos Mail and Helm] [01006A800016F04B][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Ryo Sakazaki Outfit and Wig] [01006A800016F02E][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Sans Outfit and Mask] [01006A800016F02B][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Shantae Outfit, Wig, and Song] [01006A800016F04D][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Slime Hat] [01006A800016F028][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Tails Outfit and Hat] [01006A800016F023][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Team Rocket Outfit and Hat] [01006A800016F029][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Teddie Hat] [01006A800016F021][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Tifa_s Outfit] [01006A800016F044][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Travis Outfit and Wig] [01006A800016F040][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Vault Boy Outfit and Mask] [01006A800016F03B][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Veronica_s Outfit and Hat] [01006A800016F027][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''X_s Armor and Helmet] [01006A800016F036][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate ['$'\343\200\220''Costume'$'\343\200\221''Zero_s Armor and Helmet] [01006A800016F02D][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirits Set 1 '$'\342\200\223'' Legend Support and Ace Primary] [01006A800016F083][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirits Set 1 '$'\342\200\223'' Legend Support and Ace Primary] [01006A800016F084][v0].ns" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirits Set 2 - Legend-Class Primary _ Ace-Class Support] [01006A800016F085][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Spirits Set 2 - Legend-Class Primary _ Ace-Class Support] [01006A800016F086][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Vault Shopper Set 2 -Classic Tickets and Gold for Music, Mii Costumes, and More-] [01006A800016F07C][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Vault Shopper Set 2 -Classic Tickets and Gold for Music, Mii Costumes, and More-] [01006A800016F07D][v0].nsp" '
'"/workspace/games/SSBU/Super Smash Bros Ultimate [Super Smash Bros Ultimate Fighters Pass Bonus Mii Fighter Costume Rex] [01006A800016F015][v65536].nsp" '
'''
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
time.sleep(10) # Waiting Load App
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