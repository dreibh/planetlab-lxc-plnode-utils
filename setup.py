#!/usr/bin/python

"""
Installation script for the sfa module
"""

import sys, os, os.path
from glob import glob
import shutil
from distutils.core import setup

scripts = [ "bwlimit" ] 

setup(name='plnode_utils',
      package_dir={'plnode_utils':''},
      packages='',
      scripts = scripts)
