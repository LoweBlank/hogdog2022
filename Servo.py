import Control

class Servo:
    
    def __init__(self, name, deg):
        self.name = name;
        self.deg = deg;

    def write(self, deg):
        Control.write(self.name, deg)
