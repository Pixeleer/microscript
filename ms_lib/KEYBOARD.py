import pyautogui

def lib(args):
    m = pyautogui

    if args[1] == "WRITE":
        m.typewrite(args[2])

    elif args[1] == "DRAG":
        m.drag(args[2], args[3], args[4])
    
    else:
        m.press(args[1])