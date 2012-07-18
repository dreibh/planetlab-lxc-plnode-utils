#!/usr/bin/python

import sys, os, os.path
from glob import glob
import shutil
from distutils.core import setup

scripts = [ "bwlimit" ] 

# xxx fixme
# for now we only have bwlimit.py and its flavour is selected in the main specfile
# that copies the right bwlimit_xxx.py into bwlimit.py
setup(name='plnode',
      package_dir={'plnode':'.'},
      py_modules = [ 'bwlimit' ] ,
      scripts = scripts)
