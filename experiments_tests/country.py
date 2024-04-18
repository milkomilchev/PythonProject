country = "India", "USA","Germany"

while True: 
    country = input("which coutry to select: ")

    match country: 
        case 'India':
            print("Namaste")
        case 'USA': 
            print('Hello')
        case 'Germany':
            print ('Hallo')
        

