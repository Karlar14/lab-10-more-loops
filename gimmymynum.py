userstring = input("Gimme a number greater than 100: ")
usernum = int(userstring)

while (usernum < 100):    # statement for when the termination is not true, keep loop going...
 # while usernum is less than 100
    print(str(usernum) + " is less than 100, dummy.")

    userstring = input("Try again: ")
    usernum = int(userstring)

    print("congratulations " + str(usernum) + " greater than 100! Great job!")
