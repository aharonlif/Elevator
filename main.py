from manager import Manager


def main():
    #TODO: random number
    buildings = 1
    floors = 6
    elevators = 4
    manager = Manager(buildings=buildings, floors=floors, elv=elevators)
    manager.run()
       

if __name__ == "__main__":
    main()
