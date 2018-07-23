from enum import Enum

class Material(Enum):
    steel = 1
    wood = 2

class Rocket():
    """A flyable rocket"""

    test: int = 10
    isBuilt: bool = False

    def __init__(self, topSpeed: int, material: Material):
        self.topSpeed = topSpeed
        self.material = material
        self.currentSpeed = 0

    def launch(self):

        if self.isBuilt != True:
            raise LaunchError("Failed to launch rocket", "blah blah")
        
        while self.currentSpeed < self.topSpeed:
            self.currentSpeed += 1
        else:
            print("Max Speed Achieved!")

    def build(self):
        self.isBuilt = True

class LaunchError(Exception):
    def __init__(self, message, error):
        super().__init__(message)

        self.error = error