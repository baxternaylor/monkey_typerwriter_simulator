# Possible chars the monkey will type in hex
# 0x9(tab), 0x20 - 0x7E
#in decimal 
# 9 (tab), 10(new line), 32-126 on ascii table
#implementation will have a random number generator generating numbers from 0-95, 0 maps to 9, 1 maps to 10, 2 maps to 32 and so on

import random

#open and read the text file
f = open("RomeoAndJuliet.txt", "r")
text = f.read()
f.close()

best_match = ""
current_match = ""

for x in range(0, 1_000_000):
    #gets random num
    rand_num = random.randint(0, 95)
    char = ""
    if rand_num == 0: #special case for tab
        char = chr(9)
    elif rand_num == 1: #special case for new line
        char = chr(10)
    else: #regular case can just add 30 to get to the correct decimal number for the ascii value
        char = chr(rand_num + 30)
    current_match += char

    if current_match in text:
        if len(current_match) > len(best_match):
            best_match = current_match
            print("New best match! \"" + best_match + "\"")
    else:
        current_match = ""

print("Finished! Your best match was \"" + best_match + "\"")
