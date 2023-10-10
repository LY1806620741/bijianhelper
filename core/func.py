import os
"""寻找必剪路径"""
def findBijian(args):
    os.environ['USERPROFILE']=R"D:\Users\Administrator"
    path=f"{os.environ['USERPROFILE']}\AppData\Local\BcutBilibili"
    if os.path.exists(path):
        return path