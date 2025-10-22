"""controller module"""
import numpy as np

class Controller:
    def __init__(self):
        self.K_P = 0.07
        self.K_D = 0.2

    def run_controller(self, reference_t, observation_t):
        e_t = reference_t - observation_t
        #At the very start, assume zero derivative
        try:
            e_t1 = e_t1
        except UnboundLocalError:
            e_t1 = e_t
        u = self.K_P * e_t + self.K_D * (e_t - e_t1)
        e_t1 = e_t
        return u
