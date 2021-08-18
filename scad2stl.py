from os import listdir
from subprocess import call
import os
dir = r'D:\OpenSCAD\openscad'
files = listdir(r'C:\Users\Wreathmoon\Desktop\Dataset2\cylinder\scad')
for f in files:
    if f.find(".scad") >= 0:            # get all .scad files in directory
        of = f.replace('.scad', '.stl') # name of the outfile .stl
        print(f)
        of = os.path.join(r'C:\Users\Wreathmoon\Desktop\Dataset2\cylinder\stl', of)
        f =  os.path.join(r'C:\Users\Wreathmoon\Desktop\Dataset2\cylinder\scad', f)
        cmd = 'call (["{}",  "-o", "{}",  "{}"])'.format(dir, of, f)  # create openscad command
        os.system("call " + dir + ' -o ' + of + ' ' + f)
        print(cmd)