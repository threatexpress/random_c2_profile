banner = '''
===================================================================
 ___              _              ___ ___   ___          __ _ _     
| _ \__ _ _ _  __| |___ _ __    / __|_  ) | _ \_ _ ___ / _(_) |___ 
|   / _` | ' \/ _` / _ \ '  \  | (__ / /  |  _/ '_/ _ \  _| | / -_)
|_|_\__,_|_||_\__,_\___/_|_|_|  \___/___| |_| |_| \___/_| |_|_\___|
Cobalt Strike random C2 Profile generator
Joe Vest (@joevest) - 2021
===================================================================
'''
# Cobalt Strike profile version 
version = "4.6"

print(banner)
print("[*] Generating Cobalt Strike " + version + " c2 profile...")

from jinja2 import Template
from core.variables import *

sample_name = get_random_string(8)
c2profile_template_file_contents = open("c2profile_template.jinja",'r').read()
c2profile_template = Template(c2profile_template_file_contents)

jinja2_variables = variables

variables['sample_name'] = sample_name
random_c2profile = c2profile_template.render(variables)

f = open("output/" + sample_name + '.profile', "a")
f.write(random_c2profile)
f.close()

print("[*] Done. Don't forget to validate with c2lint. ")
print("[*] Profile saved to output/" + sample_name + '.profile')



