class LinuxProcess:
    def __init__(self):
        self.inputs = input("Please enter a pid: ")
        self.filez = open("/proc/{}/stat".format(self.inputs),"r")
        self.buff = self.filez.read()

buff = LinuxProcess()
buff2 = buff.buff.split(' ')

print("name:",buff2[1].strip("()"))
print("state:", buff2[2])
print("pid:",buff2[0])
print("ppid:",buff2[3])
# Apparently the rest of the values are stored in decimal form, converted to int then hex  
print("rss: {}".format(hex(int(buff2[23]))))
print("rsslim: {}".format(hex(int(buff2[24]))))
print("start_code: {}".format(hex(int(buff2[25]))))
print("end_code: {}".format(hex(int(buff2[26]))))
print("start_stack: {}".format(hex(int(buff2[27]))))
print("start_data: {}".format(hex(int(buff2[44]))))
print("end_data: {}".format(hex(int(buff2[45]))))
print("start_brk: {}".format(hex(int(buff2[46]))))
print("arg_start: {}".format(hex(int(buff2[47]))))
print("arg_end: {}".format(hex(int(buff2[48]))))
print("env_start: {}".format(hex(int(buff2[49]))))
print("env_end: {}".format(hex(int(buff2[50]))))