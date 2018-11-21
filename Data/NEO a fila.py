# In[2]:
with open('{}.txt'.format(input('Archivo? \n'), 'r')) as p:
    rr = p.read()
	
rr = rr.split()

with open('Resultados NEOPIR.txt', 'w') as out:
	for r in rr:
		out.write(str((int(r) + 1)) + ';')
