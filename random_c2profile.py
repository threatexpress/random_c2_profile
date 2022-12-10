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

import argparse
import os.path
from re import template
from jinja2 import Template
from core.variables import *

# Default template path
default_template = "templates/default_c2profile_template.jinja"

# Description
description = 'This project is designed to generate malleable c2 profiles for Cobalt Strike. See readme for detailed help.'

# Arguments
parser = argparse.ArgumentParser(description=description)
parser.add_argument('-t', '--template', help="Path to the profile template", nargs='?', default=default_template)

args = parser.parse_args()

# Does profile exist?
if not (os.path.isfile(args.template)):
    print(f"[!] Template file not found. Check path ({args.template})")
    exit()


# Get Cobalt Strike version from variables.py
version = variables['version']

print(banner)
print(f"[*] Generating Cobalt Strike Malleable C2 Profile")
print(f"    Version : {version}")
print(f"    template: {args.template}")

sample_name = get_random_string(8)
c2profile_template_file_contents = open(args.template,'r').read()
c2profile_template = Template(c2profile_template_file_contents)

jinja2_variables = variables

variables['sample_name'] = sample_name
random_c2profile = c2profile_template.render(variables)

f = open("output/" + sample_name + '.profile', "a")
f.write(random_c2profile)
f.close()

print("[*] Done. Don't forget to validate with c2lint. ")
print("[*] Profile saved to output/" + sample_name + '.profile')



