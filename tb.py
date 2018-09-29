#MIT License
#
#Copyright (c) 2016 markgot
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

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
