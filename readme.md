# Random C2 Profile Generator

Cobalt Strike random C2 Profile generator

Author: Joe Vest (@joevest)

## Overview

This project is meant to quickly generate a random c2 profile. It is basically a Jinja template with random variables. The idea is to focus on randomization vs a cohesive set of values that support a specific threat actor.

Detailed Malleable C2 profile information can be found at https://github.com/threatexpress/malleable-c2/. 

!! OPSEC warning using the default profile !!

The default template may not meet your OPSEC needs. Profiles should always be tweaked to meet your specific needs. You can create your own profile template for customization. Custom templates can be save in the templates directory. Copy the default template and modify as needed.

### OPSEC WARNING: Highlights of the default profile you should be aware of before using

- Staging is enabled by default. You should disable this.
- The default does not support profile variants (see Profile Variants - https://www.cobaltstrike.com/help-malleable-c2)
- URIs and DNS hosts are not fancy, they are built using a random words from a word list.
- The process injection setting may not fit your OPSEC needs

## Setup

This has been designed and tested with python3

### Method 1: Keep your pythons separate and use pipenv (my prefered) - https://pipenv-fork.readthedocs.io/en/latest/basics.html

- 1st, Install pipenv for your environment
- 2nd, setup pipenv environment

```
pipenv --python 3.10
pipenv install
pipenv shell
python random_c2profile.py
```

### Method 2: Via pip3 and the Pipfile

```
git clone https://github.com/threatexpress/random_c2_profile
cd random_c2_profile
pip3 install -p Pipfile
python3 random_c2profile.py
```

## Generate some profiles

#### Generate profile from default template

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

[*] Generating Cobalt Strike Malleable C2 Profile
    Version : 4.7
    template: templates/default_c2profile_template.jinja
[*] Done. Don't forget to validate with c2lint. 
[*] Profile saved to output/UBVOTUIW.profile
```

#### Generate profile from custom template

```
python random_c2profile.py --template templates/my_template.jinja

===================================================================
 ___              _              ___ ___   ___          __ _ _     
| _ \__ _ _ _  __| |___ _ __    / __|_  ) | _ \_ _ ___ / _(_) |___ 
|   / _` | ' \/ _` / _ \ '  \  | (__ / /  |  _/ '_/ _ \  _| | / -_)
|_|_\__,_|_||_\__,_\___/_|_|_|  \___/___| |_| |_| \___/_| |_|_\___|
Cobalt Strike random C2 Profile generator
Joe Vest (@joevest) - 2021
===================================================================

[*] Generating Cobalt Strike Malleable C2 Profile
    Version : 4.7
    template: templates/my_template.jinja
[*] Done. Don't forget to validate with c2lint. 
[*] Profile saved to output/NSJOTVMN.profile
```

## File Descriptions

File                     | Description
-------------------------|------------
c2profile_template.jinja | Base template for a c2 profile
variable.py              | Mapping of python variables to variables used in jinja template. Modify these as you need. 
functions.py             | contains logic for generating data used in a profile. Additional functions can be added and used in a custom profile template.
html_contents.py         | contains a set of html code used to inject 'random' data into a profile

## References

- http://threatexpress.com/blogs/2018/a-deep-dive-into-cobalt-strike-malleable-c2/
- https://bluescreenofjeff.com/2017-01-24-how-to-write-malleable-c2-profiles-for-cobalt-strike/
- https://github.com/threatexpress/malleable-c2/
- https://github.com/FortyNorthSecurity/C2concealer/

### Magic MZ

- https://www.redteam.cafe/red-team/shellcode-injection/magic_mz_x86-and-magic_mz_x64

### Word list source

- https://raw.githubusercontent.com/chrislockard/api_wordlist/master/objects.txt
- https://raw.githubusercontent.com/chrislockard/api_wordlist/master/actions.txt

## Change Log

Note: Get change log from git using `git log --pretty=format:"  - %cd - %cn : %s"`
- Sat Dec 10 16:54:22 2022 -0600 - vestjoe : add ability to load custom profile template
- Sat Dec 10 15:43:19 2022 -0600 - vestjoe : updated readme about OPSEC, fixed dependency versions, updated pipenv 
usage instructions
- Tue Dec 6 13:24:00 2022 -0600 - vestjoe : update readme
- Tue Dec 6 13:20:54 2022 -0600 - GitHub : Merge pull request #10 from threatexpress/4.7
- Tue Dec 6 13:17:17 2022 -0600 - vestjoe : Added 4.7 profile settings, Removed old HTML content template, Added new HTML content template to html_content.py
- Wed Jun 22 11:58:22 2022 -0500 - GitHub : Merge pull request #6 from Maleick/main
- Wed Jun 22 11:57:47 2022 -0500 - GitHub : Merge pull request #5 from ceramic-skate0/patch-1
- Wed Jun 22 11:43:07 2022 -0500 - Maleick : Add Cobalt Strike version variable
- Mon May 23 13:03:28 2022 -0400 - GitHub : Update readme.md
- Wed Apr 20 18:44:19 2022 -0500 - GitHub : Merge pull request #4 from threatexpress/cs4.6
- Wed Apr 20 18:36:29 2022 -0500 - vestjoe : cs4.6 updates
- Fri Dec 17 13:44:45 2021 -0600 - vestjoe : update for CS 4.5
- Fri Dec 17 13:26:30 2021 -0600 - GitHub : Merge pull request #2 from Pernat1y/patch-1
- Sat Sep 11 14:43:27 2021 +0300 - GitHub : Updated readme
- Mon Aug 30 06:07:18 2021 -0500 - vestjoe : added 4.4 tweaks
- Mon Aug 30 06:01:47 2021 -0500 - vestjoe : silly bug
- Thu Aug 26 12:06:33 2021 -0500 - vestjoe : tweaks to DNS settings, host must be lowercase, adjusted dns_sleep options
- Mon Aug 23 12:50:47 2021 -0500 - vestjoe : Updated for CS 4.4 and added magic mz options
- Thu May 6 20:05:33 2021 -0500 - vestjoe : fix
- Thu Apr 29 11:47:00 2021 -0500 - vestjoe : update spawnto to better match x64 and x86 across mutiple version of Windows
- Wed Apr 28 13:55:57 2021 -0500 - vestjoe : better compatibility
- Sat Apr 3 15:51:24 2021 -0500 - vestjoe : updated
- Sat Apr 3 15:49:52 2021 -0500 - vestjoe : updated
- Sat Apr 3 15:26:49 2021 -0500 - vestjoe : initial