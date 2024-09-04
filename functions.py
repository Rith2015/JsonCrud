import json
import os

filename = 'cars.json'
cars = []

# Open file info
def Openfile():
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except:
        return []
# Adds new info into cars.json
def Addinfo():
    id = input("Car id is: ")
    for car in cars:
        if car['Id'] == id:
            print(f"{car['Color']} {car['Brand']} already has this Id.")
    Color = input("Car color is: ")
    Brand = input("Car brand is: ")
    cars.append({'Id': id, 'Color': Color, 'Brand': Brand})
    savedata()
# Delete car by id
def delete(action):
    id = input(f'Car to {action} is: ')
    found=False
    for i, car in enumerate(cars):
        if car['Id'] == id:
            del cars[i]
            print(f'{car['Color']} {car['Brand']} has been deleted.')
            found=True
            break
    if not found:
        print(f'Car Number {id} not found.')

# Edit car info
def editCar(action):
    oldCar = input(f"car to {action} info is: ")
    for car in cars:
        if car['Id'] == oldCar:
            print(f'{car}')
            NewColor = input("New Car color is: ")
            NewBrand = input("New Car brand is: ")
            car['Color'] = NewColor
            car['Brand'] = NewBrand
            print(f'Car {oldCar} has been updated.')
            print(f'{car}')
            savedata()
            return
    print("Car not found.")

# Search car by color and brand
def Search(action):
    color_search = input(f'{action} for which car color: ')
    brand_search = input(f'{action} for which car brand: ')
    found_cars = [(i, car) for i, car in enumerate(cars) if car['Color'].lower() == color_search.lower() and car['Brand'].lower() == brand_search.lower()]

    if found_cars:
        for i, car in found_cars:
            print(f'Car found: {car} in position {i}')
    else:
        print("Car not found.")

# Search car by id
def SearchID(action):
    id_search = input(f'{action} for which car id: ')
    found_cars = [(i, car) for i, car in enumerate(cars) if car['Id'].lower() == id_search.lower()]

    if found_cars:
        for i, car in found_cars:
            print(f'Car found: {car} in position {i}')
    else:
        print("Car not found.")

# Print the list of all items in the JSON file
def ShowAll():
    if not cars:
        print("No cars available.")
    else:
        print("All cars:")
        for car in cars:
            print(f"ID-{car['Id']}: {car['Color']} {car['Brand']}")

# Save changed data into JSON file
def savedata():
    try:
        with open(filename, 'w') as file:
            json.dump(cars, file, indent=4)
            print(f"Data saved into {filename}")
    except:
        return[]

# Close the application, save data, and clear the screen
def Exit_app():
    os.system('cls' if os.name == 'nt' else 'clear')
    savedata()
    exit()
