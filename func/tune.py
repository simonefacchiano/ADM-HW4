import subprocess
import sys

def probability(Sim, r, b):
    # s: similarity
    # r: rows (per band)
    # b: number of bands
    return 1 - (1 - Sim**r)**b

def tune():
    import pandas as pd
    import numpy as np
    results = pd.DataFrame({
        'Sim': [],
        'P': [],
        'r,b': []
    })

    for Sim in np.arange(0.01, 1, 0.01):
        total = 20
        for b in [20,10,5,4,2,1]:
            r = int(total/b)
            P = probability(Sim, r, b)
            results = pd.concat([results,pd.DataFrame({
                'Sim': Sim,
                'P': P,
                'r,b': f"{r},{b}"
            },index=[0])], ignore_index=True)

    import matplotlib.pyplot as plt
    import seaborn as sns

    sns.lineplot(data=results, x='Sim', y='P', hue='r,b').set(title='Tuning beta')
    return
