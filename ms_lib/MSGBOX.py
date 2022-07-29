import os
import time
import pymsgbox

def lib(args):
    args.remove("MSGBOX")
    str = ''
    for item in args:
        item = item.replace("\n", "")
        str = str+item+" "
    pymsgbox.alert(f'{str}', 'Microscript Output')