import numpy as np

class SIRModel:
    def __init__(self, N=None, S_init=None, I_init=None, beta=None, gamma=None):
        self.N = N
        self.S = S_init
        self.I = I_init
        self.R = 0
        self.beta = beta
        self.gamma = gamma
        self.infection_rates = []
        self.recovery_rates = []
    
    def get_dS_dt(self, S, I):
        return -self.beta * S * (I/self.N)
    
    def get_dR_dt(self, I):
        return self.gamma * I

    def get_dI_dt(self, dS_dt, dR_dt):
        return -dS_dt - dR_dt
    
    def update_compartment(self):
        dS_dt = self.get_dS_dt(self.S, self.I)
        dR_dt = self.get_dR_dt(self.I)
        dI_dt = self.get_dI_dt(dS_dt, dR_dt)

        self.S += dS_dt
        self.I += dI_dt
        self.R += dR_dt

        self.S = max(0, self.S)
        self.I = max(0, self.I)
        self.R = max(0, self.R)

        return dS_dt, dI_dt, dR_dt
    
    def compute_beta(self, S, I, N, dS_dt):
        """Calcule beta et l'ajoute toujours à la liste pour maintenir la cohérence des longueurs."""
        if S > 0 and I > 0:
            beta = -(N * dS_dt) / (S * I)
        else:
            beta = np.nan  
        self.infection_rates.append(beta)
        return beta
    
    def compute_gamma(self, I, dR_dt):
        """Calcule gamma et l'ajoute toujours à la liste pour maintenir la cohérence des longueurs."""
        if I > 0:
            gamma = dR_dt / I
        else:
            gamma = np.nan  
        self.recovery_rates.append(gamma)
        return gamma