import os
import time

def lib(args):
    args.remove("PRINT")
    str = ''
    for item in args:
        item = item.replace("\n", "")
        str = str+item+" "
    print(str)