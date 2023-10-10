import argparse
from core.i18n import _

parser = argparse.ArgumentParser(prog='bijianhelper',description=_('目前只支持windows'))
subparsers = parser.add_subparsers(help='sub-command help')
test = subparsers.add_parser('test', help='add help')
from core.func import findBijian
test.set_defaults(func=findBijian)



def Run(argv):
    args = parser.parse_args()
    args.func(args)