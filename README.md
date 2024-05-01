# Elevator
This software is used to order an elevator that is closest to the elevators in the building, so that the user will have a screen with an elevator order button, they will see an elevator arriving, the user will select the required floor where the elevator will go up. There will be separation lines between the floors
In addition, it will be possible to add additional buildings.

Software details:
The software is in Python, using the OOP method.
For this purpose, it's need 5 departments:
1. Manager (arguments) - 1. Location of the building 2. Array of elevators. 3. Location of first elevator 5. Spacing between elevators Functions - add building
1. Building (arguments 1. Number of floors, 2. Separation line.
 Function - nearest elevator (floor number) returns the nearest free elevator, if there is none, prints 'not available at the moment' and when free returns the free elevator)
2. Floor (arguments - 1. Image file name 2. Floor number.)
3. Separation lines (arguments - 1. type 2. size 3. color 4. line number)
4. Elevator (arguments - 1. Image file name 2. Floor number. 3. The elevator_is occupied (Boolean). Functions - The elevator_is_occupied (Boolean) that changes the variable in the form entered in the function value)