import os
import time
import random
import pymsgbox
import sys

libs = []

import ms_lib

class _global:
    loop = False
    
def report_error(error, file):
    pymsgbox.alert(f'Error in microscript {file}:\n{error}', 'Error')
    exit()

def run_script(f_f):
    try:
        def run():
            f = open(f_f, "r")
            
            for line in f.readlines():
                done = False

                args = line.split(" ")
                cmd = args[0]
                for module in os.listdir(r"ms_lib"):
                    module = module.upper().replace(".PY", "")
                    if module == '__init__.py':
                        continue
                    if cmd == "\n":
                        done = True
                    if cmd == "LOOP":
                        _global.loop = True
                        done = True
                    if module == cmd:
                        exec(f"import ms_lib.{module}")
                        exec(f"ms_lib.{module}.lib(args)")
                        done = True
                if done != True:
                    report_error(f"[Microscript] {cmd} | Not found.", f_f)
            
        run()

        if _global.loop == True:
            while _global.loop:
                run()

    except Exception as e:
        report_error(e, f_f)

if __name__ == "__main__":
    conf_f = open("ms.conf", "r")
    conf = conf_f.read()
    settings = conf.split("=")
    conf_f.close()
    if settings[0] == "run":
        if settings[1] == "input":
            scr = input("-> ")
            if scr == "update_dep":
                for line in open("req.txt", 'r'):
                    os.system(f"{sys.executable} -m pip install {line}")
                exit()
            run_script(scr+".micro")
        else:
            run_script(settings[1])
    else:
        report_error(f"[Microscript] \"run\" config variable not set.", "ms.conf")