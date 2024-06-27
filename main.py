from manager import Manager

def main():
    """
    Main function to initialize the Manager with a given number of buildings, 
    floors, and elevators, and start the simulation.
    """
    # TODO: Generate random number of buildings, floors, and elevators
    buildings = [{"floors": 7, "elevators" : 3},
                 {"floors": 3, "elevators" : 1},
                 {"floors": 6, "elevators" : 3},
                 {"floors": 6, "elevators" : 1}]

    manager = Manager(buildings)
    manager.run()

if __name__ == "__main__":
    """
    Entry point for the program. Calls the main function.
    """
    main()