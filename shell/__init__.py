import argparse
from core.i18n import _
parser = argparse.ArgumentParser(description=_('目前只支持windows'))
# 给这个解析对象添加命令行参数
# parser.add_argument('radius', type=int, help='Radius of cylinder')
# parser.add_argument('height', type=int, help='Height of cylinder')




def Run(argv):
    args = parser.parse_args(argv)
    from core.func import findBijian
    # parser.print_help()
    findBijian()