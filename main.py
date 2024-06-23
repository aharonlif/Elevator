from manager import Manager


def main():
    #todo: random number
    buildings = 1
    floors = 6
    elevators = 2
    manager = Manager(buildings=buildings, floors=floors, elevators=elevators)
    manager.run()
       

if __name__ == "__main__":
    main()
