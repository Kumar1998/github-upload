def printRectangle(h,w):
    for i in range(0,h):
        print("")
        for j in range(0,w):
            if (i==0 or i==h-1 or j==0 or j==w-1):
                 print("#",end="")
            else:
                print("",end="")

h=int(input("Enter Height of Rectangle:"))
w=int(input("Enter width of Rectangle:"))
printRectangle(h,w)
