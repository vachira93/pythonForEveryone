size = int(input())
if size <= 34:
    print("XS")
elif size <= 36:
    print("s")
elif size <= 38:
    print("M")
elif size <= 40:
    print("L")
else:
    print("XL")

    
m = int(input())
d = int(input())
if m % 3 == 0:
    if d < 21:
        if m == 1 or m == 2 or m == 3:
            print("Winter")
        elif m == 4 or m == 5 or m == 6:
            print("Spring")
        elif m == 7 or m == 8 or m == 9:
            print("Summer")  
        elif m == 10 or m == 11 or m == 12:
            print("Fall")  
    else:
        if m == 1 or m == 2 or m == 3:
            print("Spring")
        elif m == 4 or m == 5 or m == 6:
            print("Summer")
        elif m == 7 or m == 8 or m == 9:
            print("Fall")
        elif m == 10 or m == 11 or m == 12:
            print("Winter")

