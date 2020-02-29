# Destiny 2 Fractaline Automated Program.
Python v2.7.16

Author: pyFlummox

version: 1.3.6.7

*I have decided to release the source code as there seems to be fewer bugs than when I originally developed this program. If There are any suggestion please feel free to message me and contribute. This is not the prettiest code and it really needs to be put into a class struture. Since this event is only lasting for another week and a half I have chosen not to create a GUI or restruture the script.*

Description: This program was created for one purpose, to automate the donating and frame dismatling process of the Empyrean Foundation in Destiny 2. It uses mostly pyautogui commands with positions where mouse events happen. It gives ample delay in game so clicks are registered in-game.

Modules used: pyautogui, time, sys, cv2, os.path, os

Compiled exe link: https://drive.google.com/file/d/1ejJtq8IgvhIPe52OxwDoWNdxItANCZec/view?usp=sharing

Functionality of script:
The script has a few options in it. This script is able to pull any frame to farm for rolls or auto dismantle for shards. There is also an option for you to donate a certain number of fractaline to the obelisk. 

1)  Perfect Paradox
2)  Trophy hunter
3)  Bygones
4)  Jack Queen King
5)  Pyroclastic Flow
6)  SteelFeathered Repeater
7)  Black Scorpion-4SR
8)  Breachlight
9)  Martyr's Retribution
10) Line in the sand
11) Last Perdition
12) Infinite Paths 8
13) Gallant Charge
14) Patron of Lost Causes
15) Traveler's Judgement 5
16) Donate


**Running the program:**

1. When running the program for the first time it will ask you for you key mapping for quest and character in Destiny 2. These will be stored in a file so you don't have to enter them each time you run the program. 

2. The program will ask you which weapon you want to farm, press only the number then press enter.

3. Audo dismantle is a feature I created to dismantle all of the weapons bounties you just claimed, this is an option. Press y/n (yes/no).

4. The next prompt will ask you how many loops of x (x=4 or x=7. perfect paradox allows you get to 6-7 frames instead of 4) you want to automate.

5. After that you have 3 seconds to tab into destiny 2 and let the program begin. 


Notes:
if you are choosing not to use the auto dismantle feature I would suggest only looping the program (see **Running the program (5)**) 4-5 times as it will fill your post master x times(x=4 or x=7. perfect paradox allows you get to 6-7 frames instead of 4.)
**Legendary_lock.png* is required to be placed in the same directory as the .exe** this is just a picture of the legendary lock and the program is use the to see if weapons are locked then unlock them. 

* **If you have a 1080p monitor please download the Legendary_lock_1080.png and rename it to Lgendary_lock.png** 1080p has a different pixel density then 1440p which is what the original program was built on. 

You need the Legendary_lock.png file in the same directory as the .exe file. 


Resolution originally developed in 3440x1440 21:9 with pyautogui. I added support for 2560x1440 16:9 and 1920x1080 16:9.

The below keybinds need to be mapped in Destiny 2

'f' for dismantle

To run the exe you can run it through a shell or double click on it in Windows.  
