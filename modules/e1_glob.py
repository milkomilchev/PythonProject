import glob

myfiles= glob.glob("C:/Users/c13673e/app1/pythonProject/.venv/files/*.txt")
 
for filepath in myfiles: 
    with open (filepath, "r") as file:
        print(file.read().upper())
