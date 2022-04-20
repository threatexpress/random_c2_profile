# Random C2 Profile Generator

Cobalt Strike random C2 Profile generator

Author: Joe Vest (@joevest)

This project is designed to generate malleable c2 profiles based on the reference profile at https://github.com/threatexpress/malleable-c2/. 

## Overview

This project is meant to quickly generate a random c2 profile. It is basically a Jinja template with random variables. The idea is to focus on randomization vs a cohesive set of values that support a specific threat actor.

### Highlights you should be aware of before using

- Staging is enabled by default. You should disable this.
- This does take advantage of other good practices found in the reference profile, but adds randomization (This is why the project was created)
- Does NOT use profile variants (see Profile Variants - https://www.cobaltstrike.com/help-malleable-c2)
- URIs and DNS hosts are not fancy, they are built using a random words from a word list.

## Setup

This has been designed and tested with python3

### Method 1: Quick and easy

```
git clone https://github.com/threatexpress/random_c2_profile
cd random_c2_profile
pip3 install -r requirements.txt
python random_c2profile.py
```

### Method 2: Keep your pythons separate and use pipenv

- 1st, Install pipenv for your environment
- 2nd, setup pipevn environment

```
pipenv -python 3.8
pipenv install
pipenv shell
python random_c2profile.py
```

## Generate some profiles

```
python random_c2profile.py
===================================================================
 ___              _              ___ ___   ___          __ _ _     
| _ \__ _ _ _  __| |___ _ __    / __|_  ) | _ \_ _ ___ / _(_) |___ 
|   / _` | ' \/ _` / _ \ '  \  | (__ / /  |  _/ '_/ _ \  _| | / -_)
|_|_\__,_|_||_\__,_\___/_|_|_|  \___/___| |_| |_| \___/_| |_|_\___|
Cobalt Strike random C2 Profile generator
Joe Vest (@joevest) - 2021
===================================================================

[*] Generating Cobalt Strike 4.6 c2 profile ...
[*] Done. Don't forget to validate with c2lint. 
[*] Profile saved to output/GNAWZGHN.profile

```

## Modify this project

File | Description
-----|------------
c2profile_template.jinja | Base template for a c2 profile
variable.py | contains the default values or calls function set a specific profile setting
functions.py | contains logic for generating various profile settings

## References

- http://threatexpress.com/blogs/2018/a-deep-dive-into-cobalt-strike-malleable-c2/
- https://bluescreenofjeff.com/2017-01-24-how-to-write-malleable-c2-profiles-for-cobalt-strike/
- https://github.com/threatexpress/malleable-c2/
- https://github.com/FortyNorthSecurity/C2concealer/

Magic MZ

- https://www.redteam.cafe/red-team/shellcode-injection/magic_mz_x86-and-magic_mz_x64

# Word list source
- https://raw.githubusercontent.com/chrislockard/api_wordlist/master/objects.txt
- https://raw.githubusercontent.com/chrislockard/api_wordlist/master/actions.txt
