while(True):
    x,y,z = map(int,input().split())
    if x == 0 and y == 0 and z == 0:
        break
    
    if (x > y and x > z and x >= y+z) or (y > x and y > z and y >= x+z) or (z > y and z > x and z >= x+y):
        print("Invalid")
    elif x == y == z:
        print("Equilateral")
    elif x == y or y == z or z == x:
        print("Isosceles")
    else:
        print("Scalene")