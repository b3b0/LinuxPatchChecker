#!/usr/bin/env python

# LinuxPatchChecker - it does other stuff too!
# https://www.github.com/b3b0/LinuxPatchChecker

import sys, paramiko, os, glob
from paramiko import SSHClient, AuthenticationException, SSHException, BadHostKeyException
from paramiko.buffered_pipe import PipeTimeout as PipeTimeout
import getpass
from socket import gaierror

if len(sys.argv) < 5:
    print("Arguments missing.")
    print("Please do the following: '$ python LinuxPatchChecker.py hostname/group port username command'")
    sys.exit(1)

os.system("clear")

username = sys.argv[3]
command = sys.argv[4]
port = sys.argv[2]
#trust = sys.argv[5]
groupServsarg = sys.argv[1]
groupQuery = "/" + groupServsarg + ".srvs"
thisPath = (os.getcwd())
fullGroupPath = (thisPath + groupQuery)
isThisGroup = os.path.exists(fullGroupPath)

def machine(hostname,username,password,command,port):
    if command == "patchcheck":
        command = '[ -f /etc/centos-release ] && { OUTPUT="$(yum check-update | grep updates | grep -v updates: | wc -l)"; echo "There are ${OUTPUT} updates available"; uptime;} && [ -f /etc/lsb_release ] && { /usr/lib/update-notifier/apt-check --human-readable; uptime;}'
    print("- - - - - - - - - - - - - - -")
    print("----------------------")
    print(hostname)
    print("----------------------")
    client = paramiko.SSHClient()
    try:
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        client.connect(hostname, port=port, username=username, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        print(stdout.read())
        print("----------------------")
    except gaierror:
        print("Can't connect to that host! Does it exist? Are you online?")
    except AuthenticationException:
        print("Authentication failed, please verify your credentials")
    except SSHException:
        print("Unable to establish SSH connection")
    except BadHostKeyException:
        print("Unable to verify server's host key")
    finally:
        client.close()
def brag():
    print("""
###########################################################
## LinuxPatchChecker 1.0.4 - https://www.github.com/b3b0 ##
###########################################################
""")
brag()
if isThisGroup == True:
    with open(fullGroupPath, "r") as f:
        password = getpass.getpass()
        for line in f:
            cleanedLine = line.strip()
            if cleanedLine:
                hostname = cleanedLine
                machine(hostname,username,password,command,port)

else:
    password = getpass.getpass()
    machine(groupServsarg,username,password,command,port)
