import os
from pathlib import Path

if os.path.exists(f"{os.getcwd()}\Tools\pygettext.py"):
    os.system("python .\Tools\pygettext.py -p tmp .")

    # 翻译pot文件并移动到对应语言目录下改为po结尾

    listdir = os.listdir (".\locales")
    for i in listdir:
       
        for j in Path( f"{os.getcwd()}\locales\{i}\LC_MESSAGES").rglob("*.po"):
            os.system(f"python .\Tools\msgfmt.py {str(j)[:-3]}")
        # if os.path.exists():

else:
    print("请在项目根目录运行。please run at project root")
