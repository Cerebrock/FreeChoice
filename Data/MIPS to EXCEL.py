with open('{}.txt'.format(input('Archivo? \n'), 'r')) as p:
    r = p.read()
r = r.split()
import numpy as np
import pandas as pd
df = pd.DataFrame(r)
df = pd.get_dummies(df)
df.columns = ['F','V']
df = df[['V', 'F']]
df = df.replace(to_replace = '0', value = np.nan)
df.to_excel('Resultados.xls')