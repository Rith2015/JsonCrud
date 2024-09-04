# main.py
from enum import Enum
import os
import json
cars=[]
filename='mycars.json'
class SELECTION(Enum):
    Add = 1
    Delete = 2
    Edit = 3
    Show_all = 4
    Search_By_Color_And_Brand = 5
    Search_By_Id = 6
    Exit = 7

# Adds new info into mycars.json
def Addinfo():
    id = input("Car id is: ")
    for i, car in enumerate(cars):
        if car['Id'] == id:
            print(f"{car} already has this Id.")
            exit()
    Color = input("Car color is: ")
    Brand = input("Car brand is: ")
    cars.append({'Id': id, 'Color': Color, 'Brand': Brand})

# delete car by id
def delete(action):
    id = input(f'Car to {action} is: ')
    found = False
    for i, car in enumerate(cars):
        if car['Id'] == id:
            del cars[i]
            print(f'{car} has been found')
            found = True
            print(f'Press 7 to confirm delete of {car}.')
            break
    if not found:
        print(f'Car {id} not found.')

# edit car info that in mycars.json
def editCar(action):
    oldCar = input(f"car to {action} info is: ")
    for i, car in enumerate(cars):
        if car['Id'] == oldCar:
            print(f'{car}')
            NewColor = input("New Car color is: ")
            NewBrand = input("New Car brand is: ")
            car['Color'] = NewColor
            car['Brand'] = NewBrand
            print(f'car {oldCar} has been updated.')
            print(f'{car}')
            return i
    print("Car not found.")
    return -1

# Search car by color and brand
def Search(action):
    color_search = input(f'{action} for which car color: ')
    brand_search = input(f'{action} for which car brand: ')
    found_cars = []
    for i, car in enumerate(cars):
        if car['Color'].lower() == color_search.lower() and car['Brand'].lower() == brand_search.lower():
            found_cars.append((i, car))

    if found_cars:
        for index, car in found_cars:
            print(f'Car found: {car} in position {index}')
        return found_cars
    else:
        print("Car not found.")
        return -1

# search car by id
def SearchID(action):
    id_search = input(f'{action} for which car id: ')
    found_cars = []
    for i, car in enumerate(cars):
        if car['Id'].lower() == id_search.lower():
            found_cars.append((i, car))

    if found_cars:
        for index, car in found_cars:
            print(f'Car found: {car} in position {index}')
        return found_cars
    else:
        print("Car not found.")
        return -1

# Print the list of all items in json file
def ShowAll():
    if not cars:
        print("No cars available.")
    else:
        print("All cars:")
        for car in cars:
            print(f"ID: {car['Id']}, Color: {car['Color']}, Brand: {car['Brand']}")

# save changed data into json file/opens a new json file if there isnt one
def savedata():
    try:
        with open(filename, 'w') as file:
            json.dump(cars, file, indent=4)
            print(f"Data saved into {filename}")
    except:
        return []

# closes terminal\calls savedata function\cls terminal screen
def Exit_app():
    os.system('cls' if os.name == 'nt' else 'clear')
    savedata()
    exit()

# Open file info
def Openfile():
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except:
        return []
# open the SELECTION Menu and connect to user selection
def menu():
    for item in SELECTION:
        print(f'{item.value} - {item.name}')
    return SELECTION(int(input("Your Selection: ")))

def main():
    global cars
    cars = Openfile()
    while True:
        userselection = menu()
        if userselection == SELECTION.Add:
            Addinfo()
        elif userselection == SELECTION.Delete:
            delete('delete')
        elif userselection == SELECTION.Edit:
            editCar('edit')
        elif userselection == SELECTION.Show_all:
            ShowAll()
        elif userselection == SELECTION.Search_By_Color_And_Brand:
            Search('Search')
        elif userselection == SELECTION.Search_By_Id:
            SearchID('Search')
        elif userselection == SELECTION.Exit:
            Exit_app()
if __name__ == "__main__":
    main()
