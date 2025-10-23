"""controller module"""
import numpy as np

class Controller:
    def __init__(self):
        self.K_P = 0.06
        self.K_I = 0.007
        self.K_D = 0.9
        self.dt = 1
        # Aggregate constants for concise use & fewer calculations
        self.A = self.K_P + self.K_I*self.dt + self.K_D/self.dt
        self.B = -self.K_P - 2*self.K_D/self.dt
        self.C = self.K_D/self.dt
        # corresponding ordering in maths: e[t], e[t-1], e[t-2]
        self.e = [0,0,0]
        self.u = [0,0]


    def run_controller(self, reference_t, observation_t):
        self.e[0] = reference_t - observation_t
        self.u[0] = self.u[1] + self.A * self.e[0] + self.B * self.e[1] + self.C * self.e[2]
        self.e[2] = self.e[1]
        self.e[1] = self.e[0]
        self.u[1] = self.u[0]
        return self.u[0]
    
    def reset_controller(self):
        self.__init__()
        

