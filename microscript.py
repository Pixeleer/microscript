import os
import time
import random
import pymsgbox

libs = []

import ms_lib
    
def report_error(error, file):
    pymsgbox.alert(f'Error in microscript {file}:\n{error}', 'Error')
    exit()

def run_script(f_f):
    try:
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
                if module == cmd:
                    exec(f"import ms_lib.{module}")
                    exec(f"ms_lib.{module}.lib(args)")
                    done = True
            if done != True:
                report_error(f"[Microscript] {cmd} | Command not found.", f_f) 

    except Exception as e:
        report_error(e, f_f)

if __name__ == "__main__":
    scr = input("")
    run_script(scr+".micro")