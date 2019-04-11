
import os, sys

try:
	with open(sys.argv[1], 'r') as f:
		ret = f.read()
	print(ret)
except:
	print("Arquivo inexistente.")


