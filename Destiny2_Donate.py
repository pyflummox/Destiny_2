"""

Python v2.7.16

Author: pyFlummox version: 1.2.5.5 - does not currently support all possible frames. - mojo

Description: This program was created for one purpose, to automate the donating and frame dismatling process of 
the Empyrean Foundation in Destiny 2. It uses mostly pyautogui commands with positions where mouse events happen. 
It gives ample delay in game so clicks are registered in-game.

Modules used: pyautogui, time, sys, cv2






"""



import pyautogui
import time
import sys
import cv2
import os.path
from os import path


#Variable Declarations
Weapon_intr = 4
Donate_stonk = 4




if path.exists("saved_key_settings.txt"):
    print "saved_key_settings.txt exists"
else:
    print "Please enter the keys you use for the below actions in Destiny 2\n If you have a non-alphanumeric key please see the below list and type the same\nAny key not represented by alphanumeric or below is invalid."
    print "Caps Lock = \'capslock\'\nTab = \\t \nShift = \'shift\'\n enter = \'enter\' equal = '='"
    Inventory_Key = raw_input("Enter the key for Inventory in Destiny 2: ")
    Quest_Key = raw_input("Enter the key for Quest menu in Desiny 2: ")


    Inventory_Key = Inventory_Key.lower()
    Quest_Key = Quest_Key.lower()

    if Inventory_Key  in('capslock',"\\t",'enter','shift','=') or Inventory_Key.isalnum():
        print Inventory_Key
    else:
        print "invalid response. " + str(Inventory_Key) + " is not valid."
        quit()

    if Quest_Key  in('capslock','\\t','enter','shift','=') or Quest_Key.isalnum():
        print Quest_Key
    else:
        print "invalid response. " + str(Quest_Key) + " is not valid."
        quit()

    f = open("saved_key_settings.txt","w+")
    f.write(str(Inventory_Key) + '\n' + str(Quest_Key) + '\n')
    f.close()

f = open("saved_key_settings.txt","r")

if f.mode == 'r':
    file = f.readlines()
    Inventory_Key = file[0].strip()
    Quest_Key = file[1].strip()

f.close()

if path.exists("saved_run_settings.txt"):
    print "saved_run_settings.txt exists"
    Same_run = raw_input("Do you want to run with the same settings as last run? ")
    Same_run = Same_run.lower()
    if Same_run not in ('n','y','no','yes'):
        print "invalid response. " + auto_dismantle + " is not valid"
        quit()
    if Same_run in ('y','yes'):
        a = open("saved_run_settings.txt","r")
        
        if a.mode == 'r':
            file2 = a.readlines()
            Weapon_type = file2[0].strip()
            auto_dismantle = file2[1].strip()
            Groups_of_intr = file2[2].strip()
        a.close()
        Weapon_type = int(Weapon_type)
        Groups_of_intr = int(Groups_of_intr)
        
        if Weapon_type is 1:
            Weapon_intr = 7
            
        if Weapon_type in (2,4,7,9,11,12,13,15):
            Slot = 2
        elif Weapon_type in (1,3,6,8,14):
            Slot = 1 
        elif Weapon_type in (5,10):
            Slot = 3

        continue_quests = True
    else:

        print "pick your weapon number: \n1)  Perfect Paradox\n2)  Trophy hunter\n3)  Bygones \n4)  Jack Queen King\n5)  Pyroclastic Flow\n6)  SteelFeathered Repeater\n7)  Black Scorpion-4SR\n8)  Breachlight\n9)  Martyr's Retribution \n10) Line in the sand\n11) Last Perdition\n12) Infinite Paths 8\n13) Gallant Charge\n14) Patron of Lost Causes\n15) Traveler\'s Judgement 5\n16) Donate"
        Weapon_type = input("Enter Weapon Number: ")

        if Weapon_type not in(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16):
            print "invalid response. " + str(Weapon_type) + " is not valid"
            quit()
         
        if Weapon_type == 16:
            Donate_y = input("How much fractaline would you like to donate?: ")
            
            val = int(Donate_y)
            print "Input is an integer number. Number = " + str(val)
            Donate_stonk = val/100
            Groups_of_intr = 1
            continue_quests = False
            auto_dismantle = ''
            #except ValueError:
            #    print "invalid response. " + str(Donate_y) + " is not valid."
            #    quit()
        else:
            if path.exists("saved_run_settings.txt"):
                
                os.remove("saved_run_settings.txt")
                print "removed file"
            continue_quests = True


            if Weapon_type is 1:
                Weapon_intr = 7
                
            if Weapon_type in (2,4,7,9,11,12,13,15):
                Slot = 2
            elif Weapon_type in (1,3,6,8,14):
                Slot = 1 
            elif Weapon_type in (5,10):
                Slot = 3

                

            auto_dismantle = raw_input("Do you want to auto dismantle (n/y)? ")

            auto_dismantle = auto_dismantle.lower()

            if auto_dismantle not in ('n','y','no','yes'):
                print "invalid response. " + auto_dismantle + " is not valid"
                quit()

            Groups_of_intr = input("How many sets of Weapon type " + str(Weapon_type) + " do you want to automate? (press 0 for never ending) ")
            if Groups_of_intr is 0:
                Groups_of_intr = 100
            a = open("saved_run_settings.txt","w+")
            a.write(str(Weapon_type) + '\n' + str(auto_dismantle) + '\n' + str(Groups_of_intr) + '\n')
            a.close()
        
else:
    print "pick your weapon number: \n1)  Perfect Paradox\n2)  Trophy hunter\n3)  Bygones \n4)  Jack Queen King\n5)  Pyroclastic Flow\n6)  SteelFeathered Repeater\n7)  Black Scorpion-4SR\n8)  Breachlight\n9)  Martyr's Retribution \n10) Line in the sand\n11) Last Perdition\n12) Infinite Paths 8\n13) Gallant Charge\n14) Patron of Lost Causes\n15) Traveler\'s Judgement 5\n16) Donate"
    Weapon_type = input("Enter Weapon Number: ")

    if Weapon_type not in(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16):
        print "invalid response. " + str(Weapon_type) + " is not valid"
        quit()

    if Weapon_type == 16:
        Donate_y = input("How much fractaline would you like to donate?: ")
        
        val = int(Donate_y)
        print "Input is an integer number. Number = " + str(val)
        Donate_stonk = val/100
        Groups_of_intr = 1
        continue_quests = False
        auto_dismantle = ''
        #except ValueError:
        #    print "invalid response. " + str(Donate_y) + " is not valid."
        #    quit()
    else:
        continue_quests = True


        if Weapon_type is 1:
            Weapon_intr = 7
            
        if Weapon_type in (2,4,7,9,11,12,13,15):
            Slot = 2
        elif Weapon_type in (1,3,6,8,14):
            Slot = 1 
        elif Weapon_type in (5,10):
            Slot = 3

            

        auto_dismantle = raw_input("Do you want to auto dismantle (n/y)? ")

        auto_dismantle = auto_dismantle.lower()

        if auto_dismantle not in ('n','y','no','yes'):
            print "invalid response. " + auto_dismantle + " is not valid"
            quit()

        Groups_of_intr = input("How many sets of Weapon type " + str(Weapon_type) + " do you want to automate? (press 0 for never ending) ")
        if Groups_of_intr is 0:
            Groups_of_intr = 100

        a = open("saved_run_settings.txt","w+")
        a.write(str(Weapon_type) + '\n' + str(auto_dismantle) + '\n' + str(Groups_of_intr) + '\n')
        a.close()
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
        #print "starting loop"
        time.sleep(3)
        if Weapon_type in(1,2,3,5,6,7,8,9,10):
            #second page
            x=2850
            y=157
            if screenWidth == 2560:
                x=x-ratio_sub
            if screenWidth == 1920:
                x=1470
                y=117
            pyautogui.moveTo(x,y) 
            time.sleep(1)
            pyautogui.click()
            
        elif Weapon_type in(4,11,12,13,14,15):
            #third Page
            x=2953
            y=164
            if screenWidth == 2560:
                x = x-ratio_sub
            if screenWidth == 1920:
                x=1554
                y=119
            pyautogui.moveTo(x,y) 
            time.sleep(1)
            pyautogui.click()

        for i in range(0, Weapon_intr):
            time.sleep(1.3)
            if Weapon_type is 1:
                #Perfect Paradox
                x = 2448
                y = 329
                if screenWidth == 2560:
                    x = x-ratio_sub
                if screenWidth == 1920:
                    x=1170
                    y=273
            elif Weapon_type is 2:
                #Trophy Hunter
                x = 2574
                y = 330
                if screenWidth == 2560:
                    x = x-ratio_sub
                if screenWidth == 1920:
                    x=1281
                    y=248
            elif Weapon_type is 3:
                #Bygones
                x = 2865
                y = 818
                if screenWidth == 2560:
                    x = x-ratio_sub
                if screenWidth == 1920:
                    x=1478
                    y=610
            elif Weapon_type is 4:
                #Jack Queen King
                x = 2724
                y = 587
                if screenWidth == 2560:
                    x = x-ratio_sub
                if screenWidth == 1920:
                    x=1378
                    y=426
            elif Weapon_type is 5:
                #Pyroclastic Flow
                x=2728
                y=357
                if screenWidth == 2560:
                    x = x-ratio_sub
                if screenWidth == 1920:
                    x=1369
                    y=256
            elif Weapon_type is 6:
                #SteelFeather Repeater
                x=2700
                y=570
                if screenWidth == 2560:
                    x = x-ratio_sub
                if screenWidth == 1920:
                    x=1392
                    y=429
            elif Weapon_type is 7:
                #Black Scorpion-4SR
                x=2840
                y=589
                if screenWidth == 2560:
                    x = x-ratio_sub
                if screenWidth == 1920:
                    x=1468
                    y=418
            elif Weapon_type is 8:
                #Breachlight
                x=2978
                y=552
                if screenWidth == 2560:
                    x = x-ratio_sub
                if screenWidth == 1920:
                    x=1606
                    y=420
            elif Weapon_type is 9:
                #Martyr's Retribution
                x=2680
                y=771
                if screenWidth == 2560:
                    x = x-ratio_sub
                if screenWidth == 1920:
                    x=1352
                    y=607
            elif Weapon_type is 10:
                #Line In The Sand
                x=3021
                y=819
                if screenWidth == 2560:
                    x = x-ratio_sub
                if screenWidth == 1920:
                    x=1569
                    y=599
            elif Weapon_type is 11:
                #Last Perdition
                x=2741
                y=352
                if screenWidth == 2560:
                    x = x-ratio_sub
                if screenWidth == 1920:
                    x=1384
                    y=270
            elif Weapon_type is 12:
                #Infinite Paths 8
                x=2887
                y=316
                if screenWidth == 2560:
                    x = x-ratio_sub
                if screenWidth == 1920:
                    x=1481
                    y=237
            elif Weapon_type is 13:
                #Gallant Charge
                x=3033
                y=341
                if screenWidth == 2560:
                    x = x-ratio_sub
                if screenWidth == 1920:
                    x=1581
                    y=245
            elif Weapon_type is 14:
                #Patron of Lost Causes
                x=2888
                y=572
                if screenWidth == 2560:
                    x = x-ratio_sub
                if screenWidth == 1920:
                    x=1464
                    y=426
            elif Weapon_type is 15:
                #Traveler's Judgement 5
                x=3015
                y=571
                if screenWidth == 2560:
                    x = x-ratio_sub
                if screenWidth == 1920:
                    x=1594
                    y=446
            else:
               #print "breaking loop for weapons"
               break
            
            pyautogui.moveTo(x,y) 
            pyautogui.mouseDown()
            time.sleep(1.501)
            pyautogui.mouseUp()
        x=2748
        y=157
        if screenWidth == 2560:
            x = x-ratio_sub
        if screenWidth == 1920:
            x=1406
            y=114
        pyautogui.moveTo(x, y)
        time.sleep(.5)
        pyautogui.click()
        for j in range(0,Donate_stonk):
            #donating frac
            time.sleep(.5)
            x = 2457
            y = 328
            if screenWidth == 2560:
                x = x-ratio_sub
            if screenWidth == 1920:
                x=1168
                y=251
            pyautogui.moveTo(x,y)
            time.sleep(.5)
            pyautogui.mouseDown()
            time.sleep(3.1)
            pyautogui.mouseUp()

        if continue_quests:
            print "continue"
            print Quest_Key
            time.sleep(2)
            pyautogui.keyDown(Quest_Key)
            time.sleep(.5)
            pyautogui.keyUp(Quest_Key)
            for a in range(0,Weapon_intr):
                #time.sleep(.3)
                x = 2296
                y = 334
                if screenWidth == 2560:
                    x -= ratio_sub/2
                if screenWidth == 1920:
                    x=1383
                    y=258
                pyautogui.moveTo(x, y)
                time.sleep(.5)
                pyautogui.click()
            
        if auto_dismantle in ('y','yes'):
            #dismantling weapons
            time.sleep(2)
            if Inventory_Key in '\\t':
                pyautogui.typewrite('\t')
            else:
                pyautogui.keyDown(Inventory_Key)
                time.sleep(.5)
                pyautogui.keyUp(Inventory_Key)
            time.sleep(1)
            time.sleep(.5)
            if Slot is 2:
                x = 1151
                y = 695
                if screenWidth == 2560:
                    x -= ratio_sub/2
                if screenWidth == 1920:
                    x=520
                    y=498
                pyautogui.moveTo(x, y) #energy
                time.sleep(1)
                x=981
                y=680
                if screenWidth == 2560:
                    x -= ratio_sub/2
                if screenWidth == 1920:
                    x=418
                    y=492
                pyautogui.moveTo(x, y)
            elif Slot is 1:
                x = 1140
                y = 514
                if screenWidth == 2560:
                    x -= ratio_sub/2
                if screenWidth == 1920:
                    x=511
                    y=383
                pyautogui.moveTo(x, y) #kinetic
                time.sleep(1)
                x = 1003
                y = 522
                if screenWidth == 2560:
                    x -= ratio_sub/2
                if screenWidth == 1920:
                    x=420
                    y=383
                pyautogui.moveTo(x, y)
            elif Slot is 3:
                time.sleep(.5)
                x = 1118
                y = 844
                if screenWidth == 2560:
                    x -= ratio_sub/2
                if screenWidth == 1920:
                    x=517
                    y=631
                pyautogui.moveTo(x, y) #Heavy
                time.sleep(1)
                x = 973
                y = 834
                if screenWidth == 2560:
                    x -= ratio_sub/2
                if screenWidth == 1920:
                    x=403
                    y=632
                pyautogui.moveTo(x, y)
            for a in range(0,Weapon_intr):
                time.sleep(.5)
                lockLocation = pyautogui.locateOnScreen('Legendary_lock.png', confidence=0.9)
                if lockLocation:
                    print "found image"
                    pyautogui.keyDown('shift')
                    time.sleep(.5)
                    pyautogui.keyUp('shift')
                else:
                    print "dismantling your last hope"
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
    
   