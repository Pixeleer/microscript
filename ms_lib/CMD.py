import os
import time

def lib(args):
    args.remove("CMD")
    str = ''
    for item in args:
        item = item.replace("\n", "")
        str = str+item+" "
    os.system(str)