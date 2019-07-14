#!/usr/bin/env python3
import subprocess
# Remove APT cache
def removeaptcache(self):
    print("APTcache size is {}. Are you remove it? Y/n")

def get_aptcachesize(self):
    return subprocess.run(["echo", "${$(du", "-s", "/var/cache/apt)%%/var/cache/apt}"],stdout = subprocess.PIPE, stderr = subprocess.PIPE)

def removeit(self):
    return subprocess.run(["apt-get", "clean"], stderr = subprocess.PIPE)


# Remove old kernels
def removekernel():

    def get_oldkernels():
        #return subprocess.run(['dpkg', '--list', '|', 'grep', '-E', '-o', '"linux-image-[0-9]+\\.[0-9]+\\.[0-9]+-[0-9]+-generic"', '|', 'grep', '-o', '-E', '"[0-9]+\\.[0-9]+\\.[0-9]+-[0-9]+"', '|', 'uniq', '|', 'grep', '-E', '-v', '${dpkg', '--list', '|', 'grep', '-E', '-o', '"linux-image-[0-9]+\\.[0-9]+\\.[0-9]+-[0-9]+-generic"', '|', 'grep', '-o', '-E', '"[0-9]+\\.[0-9]+\\.[0-9]+-[0-9]+"', '|', 'uniq', '|', 'sort', '-n', '-r', '|', 'head', '-1}'],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        return 4.15 # testing

    def formating(*args):# args type = string ! Do not number
        olders = (i for i in args)
        terget = ("linux-headers-", "linux-image-")
        removed = [version + tgt for tgt in olders for version in terget]
        return removed

    def removethem(*args):
        removed = args
        return subprocess.run(["apt-get", "autoremove", "--purge", "-y", removed],stderr = subprocess.PIPE)

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

print(yesno(input()))
#removekernel()