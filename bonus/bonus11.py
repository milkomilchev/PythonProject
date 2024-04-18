try:
    width = float(input("Enter the rectangle width: "))
    lenght = float(input("Enter the rectangle lenght: "))
    if width == lenght:
        exit("That looks like a square")
        
    area = width * lenght
    print(area)
except ValueError:
    print("Enter a number. ")
