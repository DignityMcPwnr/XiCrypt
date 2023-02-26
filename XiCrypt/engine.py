import math
# Check if this file is imported correctly
def check_engine_light(color):
    engine_running = f"{color} initiated"
    return engine_running

# sets the rotors according to the code
def rotorassembly(table, Posrotor):
    I=0
    X=1
    tablelength = len(table)-1
    startletter = table[Posrotor]
    eindletter = table[tablelength]
    while startletter != str(table[0]):
        table[(tablelength-I)]= table[(tablelength-X)]
        if X == tablelength:
            I = 0
            X = 1
            table[0] = eindletter
            eindletter = table[tablelength]
        else:
            I += 1
            X += 1
    return table

# encrypts
def encrypt(letter, rotor1, rotor2, rotor3, code):
    rot1 = ((rotor1.index(letter))) #index value
    rot2 = rotor2[rot1] # letter
    rot3 = rotor3.index(rot2) #index value

    rot3 = (rot3 - code)%len(rotor3)
    
    rot2 = rotor3[rot3] #letter
    rot1 = rotor2.index(rot2) # index value
    letter = rotor1[rot1]
    return letter

#decrypts
def decrypt(letter, rotor1, rotor2, rotor3, code):
    rot1 = ((rotor1.index(letter))) #index value
    rot2 = rotor2[rot1] # letter
    rot3 = rotor3.index(rot2) #index value

    rot3 = (rot3 + code)%len(rotor3)

    rot2 = rotor3[rot3] #letter
    rot1 = rotor2.index(rot2) # index value
    letter = rotor1[rot1]
    return letter