import numpy as np
import math

class LotkaVolterra(object):
    def __init__(self, params):
        self.time = params['time']
        self.dt = params['dt']
        self.n = math.floor(self.time/self.dt)
        self.a1 = np.zeros(self.n)
        self.a1[0] = params['a1']
        self.a2 = params['a2']
        self.b1 = params['b1']
        self.b2 = params['b2']
        self.t1 = params['t1']
        self.t2 = params['t2']
        self.x1 = np.zeros(self.n)
        self.x2 = np.zeros(self.n)
        self.x1_goal = params['x1*']

        self.x1[0] = params['x1_0']
        self.x2[0] = params['x2_0']
        self.U = np.zeros(self.n)

        self.U[0] = 0.0

    def euler(self):
        self.t_goal = 0
        for i in range(0, self.n - 1):
            if i*self.dt > self.l_goal:
                return False

            x1 = self.x1[i]
            x2 = self.x2[i]
            a1 = self.a1[i]

            if x2/self.x2[0] > 10000 or x2/self.x2[0] < 0.01 or x1 <= 0 or x2 <= 0 or a1 <= 0:
                return False

            if self.t_goal == 0 and abs(x1-self.x1_goal)/self.x1_goal < 0.1:
                self.t_goal = i*self.dt
                if self.t_goal < self.l_goal:
                    self.l_goal = self.l_goal


            f1 = a1*x1-self.b1*x1*x2
            f2 = -self.a2*x2+self.b2*x1*x2

            phi = -(x1-self.x1_goal)/(self.t2*x1)+self.b1*x2
            psi = a1-phi
            dphidt = -(self.x1_goal*f1)/(self.t2*x1**2)+self.b1*f2

            if i != 0:
                self.U[i] = -(psi/self.t1)+dphidt

            self.x1[i+1] = x1+self.dt*f1
            self.x2[i+1] = x2+self.dt*f2
            self.a1[i+1] = a1+self.dt*self.U[i]

        return True

    def vals(self):
        return [self.x1, self.x2, self.a1, self.t_goal]
