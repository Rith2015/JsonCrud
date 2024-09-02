# Car Management System
## Overview
The Car Management System is a command-line application designed to manage a collection of cars. It allows users to add, delete, edit, search, and view all cars stored in a JSON file. The system uses a simple menu-driven interface for user interactions.

## Features
    Add a Car: Add a new car with an ID, color, and brand.
    Delete a Car: Remove a car by its ID.
    Edit Car Information: Update the color and brand of a car using its ID.
    Search Cars: Find cars by their color and brand or by their ID.
    Show All Cars: Display all cars currently stored in the system.
    Exit: Save changes and exit the application.
    File Structure
    mycars.json: The JSON file where car data is stored.
    car_management.py: The main Python script containing the application logic.
    Installation
    Ensure you have Python 3.x installed on your machine.
    Download or `clone the repository.
## Usage
Open a terminal or command prompt.

Navigate to the directory containing car_management.py.

Run the script using Python:

bash
Copy code
python car_management.py
Follow the on-screen instructions to use the application.
### The menu options are:

    1 - Add: Add a new car.
    2 - Delete: Delete a car by its ID.
    3 - Edit: Edit car details by its ID.
    4 - Show_all: Show all cars.
    5 - Search_By_Color_And_Brand: Search for cars by color and brand.
    6 - Search_By_Id: Search for a car by its ID.
    7 - Exit: Save data and exit the application.
### Function Descriptions
    Addinfo()
    Prompts the user for car details and adds a new car to the list if the ID does not already exist.

    delete(action)
    Prompts the user for the car ID to delete. If the car is found, it is removed from the list.

    editCar(action)
    Prompts the user for the ID of the car to edit. If found, the user can update the car's color and brand.

    Search(action)
    Prompts the user for color and brand to search. Displays matching cars and their positions.

    SearchID(action)
    Prompts the user for the car ID to search. Displays the car and its position if found.

    ShowAll()
    Displays all cars currently in the list.

    Openfile()
    Opens and reads data from mycars.json. Returns the car list.

    savedata()
    Saves the current car list to mycars.json.

    Exit_app()
    Clears the terminal, saves data, and exits the application.

    menu()
    Displays the main menu and returns the user's selection.

## Troubleshooting
    No output or errors: Ensure mycars.json is in the same directory as car_management.py.
    File read/write errors: Verify that you have the necessary permissions to read from and write to mycars.json.
## License
This project is Fake so no license. 