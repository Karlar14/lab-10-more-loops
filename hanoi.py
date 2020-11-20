# this is the hanoi code
def hanoi(n,f,h,t):   # n = number of disks, f = from position, h = helper positioq, t = target position
    if n==0:  # if the number is 0, then stop the program
        return

    hanoi(n-1,f,t,h)
    print("move disk", n, "from", f, "to", t)
    hanoi(n-1,h,f,t)


n = 4
hanoi(n,"a,","b","c") # "a" "b" "c" are the name of the sticks



    #     n = 4
    # return
