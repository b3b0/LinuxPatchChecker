# LinuxPatchChecker
Can be used for anything really though!

`python LinuxPatchChecker.py [hostname/IP/group.srvs] port username command` 

---

# How To Use
- To run a command against one server, use the following syntax:

`python LinuxPatchChecker.py hostname port username command` 

- To run a command against a LIST of servers, use the following syntax:

`python LinuxPatchChecker.py [name of .srvs file in the same directory as LinuxPatchChecker.py] port username command`

- I'm running `patchcount` against the servers in this file in this example:

![Example host list .srvs file](https://i.imgur.com/6aK6vod.png)
![patchcount](https://i.imgur.com/KONUTXi.png)

---

## Get counts of updates available with `patchcount`
![patchcount](https://i.imgur.com/KONUTXi.png)

## Get names of available updates with `patches`
![patches](https://i.imgur.com/VCbbgpj.png)

## Run any command against one or many servers!
![command](https://i.imgur.com/MMWFDXv.png)
# To Do
- Attach gif of how it works
- attach sample servers list 
- ability to have multiple hostnames
- grepping for number of updates available with a switch
