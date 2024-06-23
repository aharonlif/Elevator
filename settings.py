class Screen:
    """
    Represents the screen dimensions for the game.

    Attributes:
        width (int): Width of the screen.
        height (int): Height of the screen.
    """
    width = 1200
    height = 600


class Floor:
    """
    Represents the floor dimensions.

    Attributes:
        width (int): Width of the floor.
        height (int): Height of the floor.
    """
    width = 150
    height = 80


class Line:
    """
    Represents a line (floor separator) in the building.

    Attributes:
        color (tuple): Color of the line.
        thickness (float): Thickness of the line.
    """
    color = (0, 0, 0)
    thickness = 1/20 * Floor.height