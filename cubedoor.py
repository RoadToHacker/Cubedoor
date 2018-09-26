import socket
import socks
import requests
import base64
import sys
import argparse
import os
from modules import style
from modules import organize


def main():
	lhost = ''
	lport = ''
	rhost = ''
	rport = ''
	malw_name = ''

	# Commands loop
	global name
	name = ''
	while True:
		print(style.WHITE + '[' + style.RED +' CubeDoor'+name+' '+style.WHITE+']$' + style.WHITE, end=' ')
		command = input()
		if command.lower() == 'exit': 
			sys.exit()
	
		elif 'search' in command.lower():
			results = []
			command = command.split(' ')[1]
			
			for (path, dirs, files) in os.walk(os.getcwd()):
				for f in files:
					ff = f.replace('_', ' ')
					if command in ff:
						ff = '\033[94m'+ff.replace(' ', '_')
						results.append(ff)
						print(ff)

		elif 'use' in command.lower():
			file = command.split(' ')[1]
			name = file
			name = style.WHITE+'('+style.BLUE+ name +style.WHITE+')'
			if 'backdoor' in command.replace('_', ' '):
				while True:
					print(style.WHITE + '[' + style.RED +' CubeDoor'+name+' '+style.WHITE+']$' + style.WHITE, end=' ')
					command = input()

					if command.lower() == 'exit': 
						sys.exit()

					if 'local' in name.replace('_', ' '):

						if command.lower() == 'show options':
							if lhost == None:
								lhost = ''
							if lport == None:
								lport = ''
							if name == None:
								name = ''
							print(organize.local_backdoor_options(lhost, lport, malw_name))
						elif 'set lport' in command.lower():

							lport = command.split(' ')[2]
							print(style.WHITE+'[ '+style.GREEN+'#'+style.WHITE+' ] LPORT => %s' %(lport))

						elif 'set lhost' in command.lower():
							lhost = command.split(' ')[2]
							print(style.WHITE+'[ '+style.GREEN+'#'+style.WHITE+' ] LHOST => %s' %(lhost))

						elif 'set name' in command.lower():
							malw_name = command.split(' ')[2]
							print(style.WHITE+'[ '+style.GREEN+'#'+style.WHITE+' ] NAME => %s' %(malw_name))

						elif command.lower() == 'generate':
							organize.generate(file, lhost, lport, malw_name)

						elif command.lower() == 'main':
							main()
						else:
							print('Command not known.')

		elif command.lower() == 'help':
			print(organize.help)
      
if __name__ == '__main__':
  # setting golbals variabiles
	global lhost
	global lport
	global lhost
	global lport
	global malw_name

	print(style.banner)
	main()
