##############
#REFERENCE
##############
#https://en.wikiversity.org/wiki/Python_Concepts/Strings
#https://docs.python.org/2/library/subprocess.html
#https://www.python-course.eu/tkinter_checkboxes.php
#https://stackoverflow.com/questions/11490469/how-to-create-a-button-to-select-all-checkbuttons
##############
#import stuff for UI
##############

from Tkinter import *
root = Tk()
root.title('Show BLE Devices')
root.geometry("700x600")

##############
#import stuff for subprocess
##############

import subprocess
import os
import signal
import time

##############
#Discover devices, process the info and store in variable
##############

kill = lambda process: process.kill()
#cmd = ['ping', 'www.google.com']
#cmd = ['sudo', 'hcitool', 'lescan']
cmd = ['hcitool', 'lescan']
cmd = 'hcitool lescan'
cmd = ['timeout', '10', 'hcitool', 'lescan']
cmd = 'hcitool lescan'

process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(10)
time.sleep(3)
os.kill(process.pid, signal.SIGINT)
out = process.communicate()[0]
print out
#split based on linebreak and store lines in L array
print ("===== 1 : Print all discovered devices lines ====")
mote = []
maclist = []
for line in out.split('\n'):
    print line
    if 'Mote' in line:
        mote.append(line)
        maclist.append(line.split()[0])

print ("===== 2 : Print all Mote devices lines  ====")
print (mote)   #print stdout of proc1 to display all the Mote lines
print ("===== 3 : Print all the MAC of the Mote  ====")

#send the output from proc1 process as stdin of proc2. Basically using cut command to find the Mote MAC
#we can skip thi logic... as we will take the value from checkbox selection
#proc2 = subprocess.Popen(['cut', '-d', ' ', '-f', '1'],stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#stdout, stderr = proc2.communicate(input=stdout.encode())
#print (stdout)   #print stdout of proc2 i.e. the Mote MAC list
print ("===== 4 : Entering the UI logic  ====")

##############
#define the UI functions
##############

Label(root, text="## Discovered BLE Device MAC ## ").pack()
def create_cbuts():
    for index, item in enumerate(cbuts_text):
        boxnum.append(0)
        cbuts.append(Checkbutton(root, text = item))
        cbuts[index].pack()

def select_all():
    for i in cbuts:
        i.select()

def deselect_all():
    for i in cbuts:
        i.deselect

def var_states():
   print("Connecting to the first Mote from discovered list....: MAC is %s", maclist[0])
   #proc3 = subprocess.Popen(['gatttool', '-b', maclist[0], '-I'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
   #i = 0
   #while i < len(boxnum):
   # print boxnum[i]
   # i = i + 1

##############
#UI Processing

##############

# Create an array of check buttons for all discovered devices

#cbuts_text = out   #Assign the Lines read from hcitool cmd
cbuts_text = mote   #Assign the Lines read from hcitool cmd
cbuts = []
cbuts = []
boxnum = []
create_cbuts()

Button(root, text = 'Connect the selected MAC/Device', command=var_states).pack()
Button(root, text = 'Select all', command = select_all).pack()
Button(root, text = 'Deselect all', command = deselect_all).pack()
Label(root, text="Password: ").pack()
e1 = Entry(root)
e1.pack()

Label(root, text="SSID: ").pack()
e2 = Entry(root)
e2.pack()

Button(root, text = 'apply', command=root.quit).pack()
Button(root, text='quit', command=root.quit).pack()
mainloop()
