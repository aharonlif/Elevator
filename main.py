from manager import Manager


def main():
    #todo: random number
    buildings = 6
    floors = 10
    elevators = 3
    manager = Manager(buildings=buildings, floors=floors, elevators=elevators)
    manager.run()
       

if __name__ == "__main__":
    main()
