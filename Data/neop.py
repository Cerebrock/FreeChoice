import sys
import os
sys.path.append(os.getcwd())

try:
	from Question import question_w_options
	r = question_w_options('Neopir.txt', 5, '(.+)\s')
	with open('Resultados Neopir.txt', 'w+') as rs:
		rs.write('\n'.join(r))
except Exception as e:
	print(e)
	import time
	time.sleep(5)
