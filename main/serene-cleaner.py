#!/usr/bin/env python3
import subprocess
import re
# Remove APT cache
def removeaptcache(self):
    print("APTcache size is {}. Are you remove it? Y/n")

def get_aptcachesize(self):
    return subprocess.check_output(["echo", "${$(du", "-s", "/var/cache/apt)%%/var/cache/apt}"])

def removeit(self):
    return subprocess.check_output(["apt-get", "clean"])


# Remove old kernels
def removekernel():
    def get_oldkernels():
        output = subprocess.check_output(r'dpkg -l | grep -Eo "linux-image-[0-9]+\.[0-9]+\.[0-9]+-[0-9]" | grep -Eo "[0-9]+\.[0-9]+\.[0-9]+-[0-9]+" | uniq | sort -nr', shell=True)
        version = output.decode("UTF-8")
        installing = version.splitlines()
        del installing[0]
        olders = installing
        return olders

    def formating(*args):# args type = string ! Do not number
        olders = args[0]
        terget = ("linux-headers-", "linux-image-")
        removed = [tgt + version for version in olders for tgt in terget ]
        return removed

    def removethem(*args):
        removed = args
        return subprocess.check_output(["apt-get", "autoremove", "--purge", "-y", removed])

    #Main
    print("These kernels removed. {}".format(get_oldkernels()))
    print("Are you remove them? Y/n")
    anser = yesno(input())
    if anser == True:
        removethem(formating(get_oldkernels()))
    else:
        return 0


#Others
def yesno(choice):
    if choice == "":
        return True
    
    choice = choice[0]
    while True:
        if choice.upper() == 'Y':
            return True
        elif choice.upper() == 'N':
            return False
        else:
            return "Error"

removekernel()
