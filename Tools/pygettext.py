#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys,os,importlib
from pathlib import Path

# os.path.exists(os.environ['USERPROFILE']+"\AppData\Local")



if sys.version_info>=(3,10):
    pythonpath = sys.executable
    pygettext=Path(pythonpath+"/../Tools\i18n\pygettext.py")
    if pygettext.exists():
        os.system(pythonpath+" -X utf8 "+str(pygettext)+" "+" ".join(sys.argv[1:]))