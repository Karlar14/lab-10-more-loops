maximum_stories = int(10)
userstring = input("On what floor is your office: ")
usernum = int(userstring)

while usernum > maximum_stories:
    print("You entered: " + str(usernum) + " but there are only " + str(maximum_stories) + " floors in this building.")
    #sending the user an error message bc it is not satisfied
    userstring = input("try again: ")
    usernum = int(userstring)
   # give the user another chance to satisfy the condition

print("congratulations! " + str(usernum))
