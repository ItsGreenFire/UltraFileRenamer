import os
import shutil

'''                  ~~ DIRECTIONS ~~
    CHANGE MODE BEFORE PROCEEDING
For : MODE 0 | Integer
    STEP 0: Add files to 'UltraFileRenamer/oldfiles/'
    STEP 1: Change int value (i) to beginning number of choice.
    STEP 2 (OPTIONAL): Change incrementation to desired int
    STEP 3: Change text and file type (First set of quotes can be left blank if needed)
    STEP 4: Run program and look in 'UltraFileRenamer/newfiles/' for the renamed files
For : MODE 1 | String
    STEP 0: Add files to 'UltraFileRenamer/oldfiles/'
    STEP 1: Change array of strings (s) to how you would like. (Add or subtract strings if needed. If there aren't enough, it will repeat.)
    STEP 2: Change text and file type (First set of quotes can be left blank if needed)
    REMINDER: If you do happen to not have enough strings, make sure to change both lines marked as STEP 2 in MODE 1
    STEP 3: Run program and look in 'UltraFileRenamer/newfiles/' for the renamed files

MODES:  0 : Num
        1 : Str'''
mode = 1
rttimes = 0

#  STEP 1
i = 56
s = ["Uno", "Dos", "Tres", "Quatro", "Cinco", "Seis"]

for file in os.listdir("oldfiles"):
    #  vvv MODE 0 | Integer  vvv
    if mode == 0:
        #  STEP 2
        i += 7

        #  STEP 3
        newname = "OPTIONAL_" + str(i) + "_OPTIONAL.FILETYPE"

        shutil.move("oldfiles/" + file, "newfiles/" + newname)
    #  vvv  MODE 1 | String  vvv
    if mode == 1:
        if rttimes != len(s):
            # STEP 2
            newname = "OPTIONAL_" + s[rttimes] + "_OPTIONAL.txt"
        else:
            rttimes = 0
            # STEP 2
            newname = "OPTIONAL_" + s[rttimes] + "(" + str(rttimes) + ")" + "_OPTIONAL.txt"
        shutil.move("oldfiles/" + file, "newfiles/" + newname)
    rttimes += 1

print("All files renamed successfully")
