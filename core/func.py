import os
"""寻找必剪路径"""
def findBijian():
    
    if os.exist("$USERPROFILE\AppData\Local\BcutBilibili"):
        print("bcut")
    else:
        print("no")