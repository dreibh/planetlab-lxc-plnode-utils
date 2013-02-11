#!/usr/bin/python

import sys, os, os.path
from glob import glob
import shutil
from distutils.core import setup

scripts = [ "bin/bwlimit" ] 

# xxx fixme
# for now we only have bwlimit.py and its flavour is selected in the main specfile
# that copies the right bwlimit_xxx.py into bwlimit.py
setup(name='plnode',
      py_modules = [ 'plnode.bwlimit', 'bwlimit' ] ,
      scripts = scripts)
