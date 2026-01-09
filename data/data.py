import numpy as np
import pandas as pd

def generate_dynamic_sir_dataset(filename="../data/dynamic_software_quality_data.csv"):
    N = 1000
    days = 120
    
    S, I, R = N - 10, 10, 0
    
    dataset = []
    
    for day in range(days):
        current_beta = 0.20 + (0.15 * (day / days))
        
        
        current_gamma = 0.05 + (0.10 * np.sqrt(day / days))
        
        
        ds_dt = - (current_beta * S * I) / N
        dr_dt = current_gamma * I
        di_dt = - ds_dt - dr_dt
        
        
        new_inf = np.random.poisson(abs(ds_dt))
        new_res = np.random.poisson(dr_dt)
        
       
        new_inf = min(S, new_inf)
        new_res = min(I, new_res)
        
        
        dataset.append({
            "Day": day,
            "S": int(S),
            "I": int(I),
            "R": int(R),
            "dS_dt": round(ds_dt, 4),
            "dI_dt": round(di_dt, 4),
            "dR_dt": round(dr_dt, 4)
        })
        
        S -= new_inf
        I += new_inf - new_res
        R += new_res

    df = pd.DataFrame(dataset)
    df.to_csv(filename, index=False)
    print(f"Dynamic dataset generated: {filename}")
    return df

generate_dynamic_sir_dataset()