x=int(input("Input coordinate: "))
y=int(input("Input coordinate: "))
if x>=0 and y>=0:
    print("Coordinates in First quadrant")
elif x<=0 and y>=0:
    print("Coordinates in Second quadrant")
elif x<=0 and y>=0:
    print("Coordinates in Third quadrant")
else:
    print("Coordinates in Fourth quadrant")