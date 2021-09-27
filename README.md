# py-vrms-rpm
## A program for analyzing and listing software licenses on installed RPM packages.
[Project Github](https://github.com/christianitus03/py-vrms-rpm)

### About
py-vrms-rpm aims to replicate some of the core features of Debian's _vrms_ program, but for RPM based systems.
It is written in Python 3.9. It is currently tested & working on openSUSE Tumbleweed.

**Usage:** python3 main.py

### FAQ
* Why not a fork of Debian's VRMS?
.* Porting VRMS from .deb based systems to .rpm based systems would take a lot of work. And as my Perl skills are
    limited, I figured it would be easier to simply rewrite it myself in Python.
* Why not use [vrms-rpm](https://github.com/suve/vrms-rpm)? Why clone it?
.* For two reasons. Firstly, vrms-rpm is written in C, which is unnecessary for a program doing high level operations.
   Secondly, that implementation uses literal strings to designate approved licenses. For example:



**Usage:** python3 main.py

Please read the enclosed LICENSE.txt file for license information.

