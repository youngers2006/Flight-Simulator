# General Imports, method is same as RocketPy coz it is neat code
import numpy as np


class NoseCone():
    def __init__(self, type, length, noseRadius, rocketRadius):
        
        self.type = type
        self.noseLength = length
        self.noseRadius = noseRadius
        self.rocketRadius = rocketRadius

        # Aerodynamic Parameters
        # reference: https://offwegorocketry.com/userfiles/file/Nose%20Cone%20&%20Fin%20Optimization.pdf
        self.k = None
        self.cp = None
        self.cl = None
        self.cd = None

    def addNose(self):
    # Note the position of the nose is @ top of rocket coordinate system

        if self.type == "VonKarman":    
            self.k = 0.5
        elif self.type == "Haack":
            self.k = 0.437
        else:
            raise ValueError("Cannot find nose type?")
        
        self.geometricalParameters() # Evaluate geometrical parameters of nose
        
        self.evaluateCP()
        self.evaluateCL()
        
        # Drawing for later broooooooooooooooooo

    def geometricalParameters(self): # Finding rho, the radius ratio of nose cone
        if self.noseRadius is None or self.rocketRadius is None:
            self.radiusRatio = 1
        else:
            self.radiusRatio = self.noseRadius/self.rocketRadius
        
    def evaluateCP(self):
        self.cpx = self.k * self.noseLength
        self.cpy = 0
        self.cpz = 0
        self.cp = (self.cpx, self.cpy, self.cpz)
        return self.cp
    
    def evaluateCL(self):
        # Calculate clalpha
        # clalpha is currently a constant, meaning it is independent of Mach
        # number. This is only valid for subsonic speeds.
        # It must be set as a Function because it will be called and treated
        # as a function of mach in the simulation.
        self.clalpha = Function(
            lambda mach: 2 * self.radius_ratio**2,
            "Mach",
            f"Lift coefficient derivative for {self.name}",
        )
        self.cl = Function(
            lambda alpha, mach: self.clalpha(mach) * alpha,
            ["Alpha (rad)", "Mach"],
            "Cl",
        )
        return None

#     def evaluateCD(self):
