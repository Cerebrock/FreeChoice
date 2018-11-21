import sys
import os
sys.path.append(os.getcwd())
try:
	from Question import question_w_options
	r = question_w_options('MIPS.txt', 2, '\d.\t(.+)\.')
	with open('Resultados Mips.txt', 'w+') as rs:
		rs.write('\n'.join(r))
except Exception as e:
	import time
	print(e)
	time.sleep(5)