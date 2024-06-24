# Elevator System

Overview
This software simulates an elevator system in a building. The system allows users to call the closest available elevator to their floor. Users can see the elevator arriving, select the desired floor, and watch the elevator move between floors. The software supports multiple buildings, each with multiple floors and elevators. Separation lines are drawn between floors for visual clarity.

Software Details
The software is developed in Python using the Object-Oriented Programming (OOP) approach. It is organized into several key components:

1. Manager
The Manager class is responsible for overseeing the entire system, including the buildings and elevators.

Arguments:
buildings: The number of buildings.
floors: The number of floors in each building.
elevators: The number of elevators in each building.
Functions:
factory_of_buildings(floors, elevators): Initializes and adds buildings to the system.
check_floor_click(mouse_pos): Checks if a floor button was clicked and handles the elevator call.
update(): Updates the state of all buildings and elevators.
run(): Main loop to run the simulation.

2. Building
The Building class represents a building with multiple floors and elevators.

Arguments:
floors: The number of floors in the building.
elevators: The number of elevators in the building.
building_number: Identifier for the building (default is 0).
x_position: The x-coordinate position of the building (default is 0).
Functions:
calculate_x_position(): Calculates the x position for the building.
floors_factory(): Creates floors for the building.
elevators_factory(elevators): Creates elevators for the building.
_find_nearest_elevator(floor): Finds the nearest available elevator to the specified floor.
move_elevator(floor): Moves the nearest available elevator to the specified floor.
change_button_color(floor): Changes the color of a floor button temporarily.
update(): Updates the state of all elevators and handles elevator calls.

3. Floor
The Floor class represents a floor in a building.

Arguments:
floor_number: The floor number.
bottomleft: The bottom-left position of the floor.
Functions:
update_time_elevator(arrival_time): Updates the display to show the arrival time of the elevator.
draw_button(): Draws the button on the floor.

4. Line
The Line class represents a separation line between floors.

Arguments:
bottomleft: The bottom-left position of the line.

5. Elevator
The Elevator class represents an elevator.

Arguments:
bottomleft: The bottom-left position of the elevator.
Functions:
moving(): Checks if the elevator is moving.
move_to_floor(floor): Moves the elevator to the specified floor.
calculate_position_to_move(): Calculates the new position of the elevator.
passed_2_seconds(): Checks if two seconds have passed since the last movement.
update_location(): Updates the elevator's position.
arrived(): Checks if the elevator has arrived at the desired floor.

6. Button
The Button class represents a button on a floor to call an elevator.

Arguments:
number: The number on the button.
position: The position of the button.
color: The initial color of the button (default is light yellow).
Functions:
create_button_image(): Creates the visual representation of the button.
check_click(pos): Checks if the button was clicked.
change_color_temporarily(new_color, duration): Changes the color of the button temporarily.
reset_color(): Resets the button to its original color.