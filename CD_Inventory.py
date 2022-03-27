#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# Amalavia, 2022-Mar-26, Created File
# Amalavia, 2022-Mar-27, Modified the code to add functions to add tracks
# Amalavia, 2022-Mar-27, Added code to the select_cd mtehod and add_track methods
#------------------------------------------#

import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be cancelled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = ''
        while True:
            cd_idx = input('Select the CD / Album index: ')
            try:
                cd_idx = int(cd_idx)
                break
            except:
                print('\nThe CD Index is a numerical value! \nPlease try again.')
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)
        # TODone add code to handle tracks for an individual cd
        while True:
            IO.ScreenIO.print_CD_menu()
            strChoice = IO.ScreenIO.menu_CD_choice()
            if strChoice == 'x':
                break
            if strChoice == 'a':
                TrkInfo = IO.ScreenIO().get_track_info()
                PC.DataProcessor.add_track(TrkInfo, cd)
            elif strChoice == 'd':
                IO.ScreenIO.show_tracks(cd)
                flag = 1
                while flag:
                    print('You must enter track information to proceed')
                    flag = 0
                    continue
            elif strChoice == 'r':
                IO.ScreenIO.show_tracks(cd)
                flag = 1
                while flag:
                    trk_idx = input('Please select the Track ID: ')
                    try:
                        trx_idx = int(trk_idx)
                        flag = 0
                    except:
                        print('Track index must be an integer')
                cd.rmv_track(trk_idx)
            else:
                print('General Error')
                      
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')