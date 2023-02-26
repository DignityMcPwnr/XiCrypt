import argparse
import os
import sys
sys.path.append("/XiCrypt")
import engine

# The looks
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print (bcolors.HEADER+"")
print(" ____   ____.___ ._______ .______   ____   ____._______ _____._")
print(" \   \_/   /: __|:_.  ___\: __   \  \   \_/   /: ____  |\__ _:|")
print("  \___ ___/ | : ||  : |/\ |  \____|  \___ ___/ |    :  |  |  :|")
print("  /   _   \ |   ||    /  \|   :  \     |   |   |   |___|  |   |")
print(" /___/ \___\|   ||. _____/|   |___\    |___|   |___|      |   |")
print("            |___| :/      |___|                           |___|")
print("                  :                                            ") 
print(bcolors.OKCYAN+"Version 2.0; updated 26/02/2023")
print (""+bcolors.ENDC)

# Setting the arguments
parser = argparse.ArgumentParser(description=bcolors.WARNING+'Waring! This program is case sensitive!'+bcolors.ENDC)
parser.add_argument('-M', metavar='e/d', dest='mode', type=str, required=True, choices={'e','d'}, help='Encryption or decryption mode')
parser.add_argument('-I', metavar='<path>', dest='inputpath', type=str, required=True, help='The path to the inputfile')
parser.add_argument('-O', metavar='<path>', dest='outputpath', type=str, required=False, help='The path to the outputfile')
parser.add_argument('-S', metavar='123456', type=int, dest='code', default='123456', help='Security code. Default=123456')
parser.add_argument('-T', metavar='CNP', type=str, dest='tables', default='CNP',choices={'C','N','P','CN','NP','CP','NC','PN','PC','CNP','NPC','CPN','NCP','PNC','PCN'}, help='Select the tables (C= Upper and Lower Case, N = Numbers, P = Punctuation marks)')
args = parser.parse_args()

# Making vars from the arguments
mode = args.mode
inputpath = args.inputpath
outputpath = args.outputpath
code = args.code
tables = args.tables

# Checking input filepath

if os.path.isfile(inputpath):
    print("Inputfile found. checking file format...")
else:
    print(bcolors.FAIL+"ERROR: Inputtfile not found."+bcolors.ENDC)
    quit()

if ".txt" in inputpath and mode == "e":
    print(bcolors.OKGREEN+"File valid"+bcolors.ENDC)
    print("Loading file...")
elif ".txt" in inputpath and mode == "d":
    print(bcolors.FAIL+"ERROR: Inputfile has wrong extension (.xic required)"+bcolors.ENDC)
    quit()
elif ".xic" in inputpath and mode == "e":
    print(bcolors.FAIL+"ERROR: Inputfile has wrong extension (.txt required)"+bcolors.ENDC)
    quit()
elif ".xic" in inputpath and mode == "d":
    print(bcolors.OKGREEN+"File valid"+bcolors.ENDC)
    print("Loading file...")
else:
    print(bcolors.FAIL+"ERROR: Inputfile has wrong extension"+bcolors.ENDC)
    quit()

#checking outputfilepath
if outputpath == None:
    print(bcolors.WARNING+"No outputfile entered, new file will be created"+bcolors.ENDC)
    if mode == "e":
        outputpath = "encrypted.xic"
    else:
        outputpath = "decrypted.txt"
else:
    if os.path.isfile(outputpath):
        answer = input(bcolors.WARNING+"Outputfile found, do you wish to overwrite it? y/n: "+bcolors.ENDC)
        while answer != "y" and answer != "n":
            answer = input(bcolors.WARNING+"Do you wish to overwrite the file? y/n: "+bcolors.ENDC)
        if answer == "n":
            print("please select another file")
            quit()
        if answer == "y":
            if ".txt" in outputpath and mode == "e":
                print(bcolors.FAIL+"ERROR: Outputfile has wrong extension (.xic required)"+bcolors.ENDC)
                quit()
            elif ".txt" in outputpath and mode =="d":
                print(bcolors.OKGREEN+"File valid"+bcolors.ENDC)
                print("Loading file...")
            elif ".xic" in outputpath and mode =="e":
                print(bcolors.OKGREEN+"File valid"+bcolors.ENDC)
                print("Loading file...")
            elif ".xic" in outputpath and mode == "d":
                print(bcolors.FAIL+"ERROR: Outputfile has wrong extension (.txtrequired)"+bcolors.ENDC)
                quit()
            else:
                print(bcolors.FAIL+"ERROR: Outputfile has wrong extension"+bcolors.ENDC)
                quit()
    else:
        print("Outputfile not found, new file will be created")
        if mode == "e":
            f = open("encrypted.xic", "x")
            outputpath = "encrypted.xic"
        else:
            f= open("decrypted.txt", "x")
            outputpath = "decrypted.txt"

# Loading filetext into array
file = open(inputpath)
if os.stat(inputpath).st_size == 0:
    print(bcolors.FAIL+"Error: Failed to import filedata"+bcolors.ENDC)
    quit()
filecontent= []
for line in file:
    for character in line:
        filecontent += [character]

# Checking Security code arguement
if len(str(code)) == 6:
    print(bcolors.OKGREEN+"Securitycode is valid"+bcolors.ENDC)
else:
    print(bcolors.FAIL+"ERROR: Invalid security code"+bcolors.ENDC)
    quit()

# Creating tables
print(bcolors.OKGREEN+"Tables selected"+bcolors.ENDC)
print("Creating tables... ")

Alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
MasterTable = ['q','t','l','n','z','i','b','v','d','h','e','k','a','o','j','c','m','s','u','y','p','x','g','r','f','w','\n']
UpperCase = ['Q','L','O','F','N','Y','D','T','H','S','G','W','V','I','B','X','P','A','M','U','J','E','R','C','Z','K']
Numbers = ['1','6','8','0','7','5','3','4','9','2']
Punctuation = ["+",",","=","?",")",".","/"," ","(",";","!","-"]

if "C" in tables:
    MasterTable += UpperCase
if "N" in tables:
    MasterTable += Numbers
if "P" in tables:
    MasterTable += Punctuation
if len(MasterTable) > 28:
    print(bcolors.OKGREEN+"Tables created succesfully"+bcolors.ENDC)
else:
    print(bcolors.FAIL + "Error: Could not load tables")
    quit()

#Checking engine import
start_engine = engine.check_engine_light("Rotors")
print (bcolors.OKGREEN+start_engine+bcolors.ENDC)

# Encryption
if mode == "e":
    print("Encrypting...")

    x=0
    encryptedfile = ""

    while x < len(filecontent):

        #Setting rotor positions in the loop to rotate the rotors
        code = str(code)

        MasterTable1 = [n for n in MasterTable]
        PosRotor1 = int(code[0]+code[1])
        PosRotor1 %= len(MasterTable1)
        rotor1 = engine.rotorassembly(MasterTable1, PosRotor1)

        MasterTable2 = [n for n in MasterTable]
        PosRotor2 = int(code[2]+code[3])
        PosRotor2 %= len(MasterTable2)
        rotor2 = engine.rotorassembly(MasterTable2, PosRotor2)


        MasterTable3 = [n for n in MasterTable]
        PosRotor3 = int(code[4]+code[5])
        PosRotor3 %= len(MasterTable3)
        rotor3 = engine.rotorassembly(MasterTable3, PosRotor3)

        # Parsing to encryption
        encletter = engine.encrypt(filecontent[x], rotor1, rotor2, rotor3, PosRotor3)
        encryptedfile = encryptedfile + encletter
        x +=1
        if code == "000000":
            code = "999999"
        else:
            code = int(code)
            code -= 1

    if encryptedfile == "":
        print(bcolors.FAIL+"Error: Failed to encrypt filedata"+bcolors.ENDC)
        quit()

    print(bcolors.OKGREEN+"Encryption succesfull!"+bcolors.ENDC)

    # Writing data to file
    with open(outputpath, "w") as text_file:
        print(f"{encryptedfile}", file=text_file)
        print(bcolors.OKGREEN+"Data written to file"+bcolors.ENDC)
        
    if os.stat(outputpath).st_size == 0:
        print(bcolors.FAIL+"Error: Failed to write encrypted data to file"+bcolors.ENDC)
        quit()
# Decryption
else:
    print ("Decrypting...")

    x=0
    decryptedfile = ""

    while x < (len(filecontent)-1):
        #Setting rotor positions in the loop to rotate the rotors
        code = str(code) #123456

        MasterTable1 = [n for n in MasterTable]
        PosRotor1 = int(code[0]+code[1])
        PosRotor1 %= len(MasterTable1)
        rotor1 = engine.rotorassembly(MasterTable1, PosRotor1)

        MasterTable2 = [n for n in MasterTable]
        PosRotor2 = int(code[2]+code[3])
        PosRotor2 %= len(MasterTable2)
        rotor2 = engine.rotorassembly(MasterTable2, PosRotor2)


        MasterTable3 = [n for n in MasterTable]
        PosRotor3 = int(code[4]+code[5])
        PosRotor3 %= len(MasterTable3)
        rotor3 = engine.rotorassembly(MasterTable3, PosRotor3)

        # Parsing to decryption
        decletter = engine.decrypt(filecontent[x], rotor1, rotor2, rotor3, PosRotor3)
        decryptedfile = decryptedfile + decletter
        x +=1
        if code == "000000":
            code = "999999"
        else:
            code = int(code)
            code -= 1

    if decryptedfile == "":
        print(bcolors.FAIL+"Error: Failed to decrypt filedata"+bcolors.ENDC)
        quit()

    print(bcolors.OKGREEN+"Decryption succesfull!"+bcolors.ENDC)

    # Writing data to file
    with open(outputpath, "w") as text_file:
        print(f"{decryptedfile}", file=text_file)
        print(bcolors.OKGREEN+"Data written to file"+bcolors.ENDC)
        
    if os.stat(outputpath).st_size == 0:
        print(bcolors.FAIL+"Error: Failed to write decrypted data to file"+bcolors.ENDC)
        quit()
