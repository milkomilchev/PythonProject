def get_avarage():
    with open("C:/Users/c13673e/app1/pythonProject/.venv/bonus/files/data.txt", "r") as file: 
        data = file.readlines()

    values = data[1:]
    values = [float(i) for i in values]
    avarage_local = sum(values) / len(values)
    return avarage_local           


avarage = get_avarage()
print(avarage)