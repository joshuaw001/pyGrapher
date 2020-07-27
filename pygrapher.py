from math import *
import turtle
import string

class GraphStyle:
    pass

class Equation:
    pass

class axis:
    X_AXIS = 1
    Y_AXIS = 2
    
    #POLAR_GRID       = [0,math.PI]
    #LOGARITHMIC_GRID = [1,10]
    STANDARD_GRID     = [5,5]
    INTEGER_GRID      = [1,1]
    DECIMAL_GRID      = [0.1,0.1]
    FRACTION_1_2_GRID = [1/2,1/2]
    
    def __init__(self, x_on=True, y_on=True):
        pass
class GraphArea:
    def __init__(self, width, height, style=GraphStyle(),eqs=[Equation("y=x")]):
        self.width  = width
        self.height = height
        self.style  = style
        self.equations = eqs
        
    def reset():
        turtle.reset()
        turtle.home()
        turtle.clear()
    def draw():
        pass
