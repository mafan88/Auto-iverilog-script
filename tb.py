import os

f = os.path.dirname(os.path.realpath(__file__))

v = []
w = ''

for file in os.listdir(f):
    if file.endswith(".v"):
        v.append(file)
    elif file.endswith(".wave"):
        w = file

testbench = 'tb'

#optional
v.insert(0, v.pop(v.index("top.v")))
v.insert(0, v.pop(v.index(testbench+".v")))

commands = []
commands.append("iverilog -o "+testbench+" "+" ".join(v))
commands.append("vvp "+testbench)
commands.append("start /B gtkwave "+testbench+".vcd "+w)

def title(txt, width = 30):
    print "-"*width
    print " "*((width - len(txt))/2)+txt
    print "-"*width

title("executing iverilog")

for i in commands:
    print "executing: '"+i+"'"
    sts = os.system(i)
    #print "exit status: "+str(sts)
    if sts > 0:
        break
    
    
title("iverilog done")