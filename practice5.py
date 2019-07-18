x = 10
y = 15
z = 20
while x > y:
    print(f"x{x} y{y}")
    x -= 1
    y +=1
if x > y:
    print("Hello")
else:
    if z > y and z > x:
        print("Wow")
        if y < x:
            print("yes")
        else:
            print("No")
    else:
        print("Okay")
