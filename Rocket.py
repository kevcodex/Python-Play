from enum import Enum

class Material(Enum):
    steel = 1
    wood = 2

class Rocket():
    """A flyable rocket"""

    test: int = 10

    def __init__(self, topSpeed: int, material: Material):
        self.topSpeed = topSpeed
        self.material = material
        self.currentSpeed = 0

    def launch(self):
        while self.currentSpeed < self.topSpeed:
            self.currentSpeed += 1
        else:
            print("Max Speed Achieved!")

