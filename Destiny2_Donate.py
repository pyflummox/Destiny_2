import pyautogui
import time
import sys
import cv2




Weapon_intr = 4
print "pick your weapon number: \n1) Perfect Paradox\n2) Trophy hunter\n3) Bygones \n4) Jack Queen King"
Weapon_type = input("Enter Weapon Number: ")

if Weapon_type not in(1,2,3,4):
    print "invalid response. " + str(Weapon_type) + " is not valid"
    quit()

if Weapon_type is 1:
    Weapon_intr = 7
    
if Weapon_type in (2,4):
    Slot = 2
else:
    Slot = 1 

auto_dismantle = raw_input("Do you want to auto dismantle (n/y)? ")

auto_dismantle = auto_dismantle.lower()

if auto_dismantle not in ('n','y','no','yes'):
    print "invalid response. " + auto_dismantle + " is not valid"
    quit()

Groups_of_intr = input("How many sets of Weapon type " + str(Weapon_type) + " do you want to automate? (press 0 for never ending) ")

if Groups_of_intr is 0:
    Groups_of_intr = 100


print('Press Ctrl-C to quit.')

print "\nPlease tab into Destiny 2"
time.sleep(3)

screenWidth, screenHeight = pyautogui.size()

if screenWidth == 2560:
    ratio_sub = 880
    
elif screenWidth == 1920:
    ratio_sub = 1520

try:
    for q in range(0,Groups_of_intr):
        time.sleep(3)
        if Weapon_type != 4:
            x=2850
            if screenWidth == 2560:
                x=x-ratio_sub
            pyautogui.moveTo(x, 157)

        elif Weapon_type is 4:
            x=2953
            if screenWidth == 2560:
                x = x-ratio_sub
                
            pyautogui.moveTo(x,164) #Jack Queen King
        time.sleep(.5)
        pyautogui.click()
        for i in range(0, Weapon_intr):
            time.sleep(1)
            if Weapon_type is 1:
                x = 2448
                if screenWidth == 2560:
                    x = x-ratio_sub
                pyautogui.moveTo(x,329) #Perfect Paradox
            elif Weapon_type is 2:
                x = 2574
                if screenWidth == 2560:
                    x = x-ratio_sub
                pyautogui.moveTo(x,330) #Trophy Hunter
            elif Weapon_type is 3:
                x = 2865
                if screenWidth == 2560:
                    x = x-ratio_sub
                pyautogui.moveTo(x,818) #Bygones
            elif Weapon_type is 4:
                x = 2724
                if screenWidth == 2560:
                    x = x-ratio_sub
                pyautogui.moveTo(x,587) #Jack Queen King
            pyautogui.mouseDown()
            time.sleep(1.501)
            pyautogui.mouseUp()
        x=2748
        if screenWidth == 2560:
            x = x-ratio_sub
        pyautogui.moveTo(x, 157)
        time.sleep(.5)
        pyautogui.click()
        for j in range(0,4):
            #donating frac
            time.sleep(.5)
            x = 2457
            if screenWidth == 2560:
                x = x-ratio_sub
            pyautogui.moveTo(x,328)
            time.sleep(.5)
            pyautogui.mouseDown()
            time.sleep(3.1)
            pyautogui.mouseUp()
        time.sleep(2)
        pyautogui.keyDown('p')
        time.sleep(.5)
        pyautogui.keyUp('p')
        for a in range(0,Weapon_intr):
            time.sleep(.3)
            x = 2296
            if screenWidth == 2560:
                x -= ratio_sub/2
            pyautogui.moveTo(x, 334)
            time.sleep(.5)
            pyautogui.click()
        if auto_dismantle in ('y','yes'):
            #dismantling weapons
            time.sleep(2)
            pyautogui.typewrite('\t')
            time.sleep(1)
            time.sleep(.5)
            if Slot is 2:
                x = 1151
                if screenWidth == 2560:
                    x -= ratio_sub/2
                pyautogui.moveTo(x, 695) #energy
                time.sleep(1)
                x=981
                if screenWidth == 2560:
                    x -= ratio_sub/2
                pyautogui.moveTo(x, 680)
            elif Slot is 1:
                x = 1140
                if screenWidth == 2560:
                    x -= ratio_sub/2
                pyautogui.moveTo(x, 514) #kinetic
                time.sleep(1)
                x = 1003
                if screenWidth == 2560:
                    x -= ratio_sub/2
                pyautogui.moveTo(x, 522)
            for a in range(0,Weapon_intr):
                time.sleep(.5)
                lockLocation = pyautogui.locateOnScreen('Legendary_lock.png', confidence=0.9)
                if lockLocation:
                    print "found image"
                    pyautogui.keyDown('shift')
                    time.sleep(.5)
                    pyautogui.keyUp('shift')
                else:
                    print "dismantling"
                #1
                pyautogui.keyDown('F')
                time.sleep(1)
                pyautogui.keyUp('F')
                time.sleep(.5)
        time.sleep(.5)
        pyautogui.keyDown('esc')
        time.sleep(1)
        pyautogui.keyUp('esc')
            
        
        
    
except KeyboardInterrupt:
    print('\n')