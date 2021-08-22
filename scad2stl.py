from os import listdir
from subprocess import call
import os
dir = r'path of OpenScad.exe'
files = listdir(r'path')
for f in files:
    if f.find(".scad") >= 0:            # get all .scad files in directory
        of = f.replace('.scad', '.stl') # name of the outfile .stl
        print(f)
        of = os.path.join(r'path of stl files', of)
        f =  os.path.join(r'path of scad files', f)
        cmd = 'call (["{}",  "-o", "{}",  "{}"])'.format(dir, of, f)  # create openscad command
        os.system("call " + dir + ' -o ' + of + ' ' + f)
        print(cmd)
