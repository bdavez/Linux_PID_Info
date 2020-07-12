import os 

class LinuxProcList:
    def proclist():
        proclist = os.listdir("/proc") 
        for x in proclist:
            if x.isdigit() == True: #Wanted to print only directories with a pid
                print(x, end=', ') # Using end with print to optimize space for output
        print('')

    def cmdline(pid):
        filez = open("/proc/{}/cmdline".format(pid),"r")
        rofl = filez.read()
        filez.seek(0)
        if not filez.read(1): #Will determine if file is empty, if it is print none
            print("none")
        else:
            print(rofl)

    def children(pid):
        filez = open("/proc/{}/task/{}/children".format(pid,pid),"r")
        rofl = filez.read()
        rofl = rofl.split(' ')
        rofl.pop()
        for x in rofl:
            print(x, end=', ')
        print('')

LinuxProcList.proclist()
pid = input("Please enter a pid: ")
LinuxProcList.cmdline(pid)
LinuxProcList.children(pid)