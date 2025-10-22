"""controller module"""
import numpy as np

class Controller:
    def __init__(self):
        self.K_P = 0.07
        self.K_D = 0.8
        self.e_t = 0
        self.e_t1 = False

    def run_controller(self, reference_t, observation_t):
        self.e_t = reference_t - observation_t
        #At the very start, assume zero derivative
        if not self.e_t1:
            self.e_t1 = self.e_t
        u = self.K_P * self.e_t + self.K_D * (self.e_t - self.e_t1)
        self.e_t1 = self.e_t
        return u
    
    def reset_controller(self):
        self.__init__()
        

