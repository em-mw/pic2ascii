import os

#defining the terminal executer:

if os.environ["TERM"].find("xterm") != int(-1):
	term = 'xterm'
else:
	tterm = list(os.environ["TERM"])
	term = []
	for thing in range(len(tterm)):
		print(thing)
		if tterm[int(thing)].find('-') != int(-1):
			term = str(term)
			term = term.replace('[', '')
			term = term.replace(']', '')
			term = term.replace(',', '')
			term = term.replace(' ', '')
			term = term.replace('\'', '')
			del tterm
			break
		else:
			term.append(tterm[int(thing)])
print(term)