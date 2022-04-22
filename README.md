# py-vrms-rpm
## A program for analyzing and listing the software licenses of installed RPM packages.
[Project Github](https://github.com/christianitis/py-vrms-rpm)

### About
py-vrms-rpm aims to replicate some of the core features of Debian's _vrms_ program, but for RPM based systems.
It has been tested & is confirmed working on openSUSE Tumbleweed.

#### License
This program is licensed under the GNU Public License Version 3. 
Please read the included COPYING file for license information.

### Dependencies
* Python 3 or above.
* rpm 
* You may also need to install the python3-rpm package via your system's native package manager.

### FAQ
**Usage:** python3 py-vrms-rpm.py

* Why not a fork of Debian's VRMS?

Porting VRMS from .deb based systems to .rpm based systems would take a lot of work. And as my Perl skills are
limited, I figured it would be easier to simply rewrite it myself in Python.

* Why not use [vrms-rpm](https://github.com/suve/vrms-rpm)? Why clone it?

Don't get me wrong: I find that project very commendable. However, I have two reasons for creating a seperate program.
Firstly, vrms-rpm is written in C, which is unproductive for a program performing high level operations (such as text processing).
Secondly, that implementation uses literal strings to designate approved licenses. For example, a package with
the license text **GPL3-0 AND MIT** may not work because of case sensitivity or a "malformed" license string (GPL3-0 rather
than, say; GPL3). py-vrms-rpm takes a different approach: instead of using literal strings, it uses keywords (such as
"GPL" and "MIT") to determine if the package is free. Similarly, it also uses keywords such as "FIRMWARE" or "PROPRIETARY"
to determine if a package is non-free or contains non-free parts. This avoids many of the problems associated with using
entire literal strings for license determination.
