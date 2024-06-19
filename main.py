from manager import Manager


def main():
    #TODO: random number
    buildings = 1
    floors = 5
    elevators = 2
    manager = Manager(buildings=buildings, floors=floors, elv=elevators)
    manager.run()
       

if __name__ == "__main__":
    main()
