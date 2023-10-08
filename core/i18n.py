from gettext import translation
import os

root_dir = os.path.join(os.path.dirname(__file__),"..","locales")

zh = translation(domain="messages", localedir='locales', languages=["en","zh"])
# zh.install()
_ = zh.gettext

def __init__():
    pass