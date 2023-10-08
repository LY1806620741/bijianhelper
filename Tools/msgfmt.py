import sys,os
from pathlib import Path

if sys.version_info>=(3,10):
    pythonpath = sys.executable
    pygettext=Path(pythonpath+"/../Tools\i18n\msgfmt.py")
    if pygettext.exists():
        os.system(pythonpath+" "+str(pygettext)+" "+" ".join(sys.argv[1:]))