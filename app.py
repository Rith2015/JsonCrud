from enum import Enum
from functions import Addinfo, delete, editCar, ShowAll, Search, SearchID, Exit_app, Openfile, cars

class SELECTION(Enum):
    Add = 1
    Delete = 2
    Edit = 3
    Show_all = 4
    Search_By_Color_And_Brand = 5
    Search_By_Id = 6
    Exit = 7

# Display the menu and handle user selection
def menu():
    for item in SELECTION:
        print(f'{item.value} - {item.name}')
    return SELECTION(int(input("Your Selection: ")))

def main():
    global cars
    cars.extend(Openfile())  # Load cars data into the global list
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
