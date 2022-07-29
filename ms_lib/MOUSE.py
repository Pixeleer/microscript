import pyautogui

def lib(args):
    m = pyautogui

    if args[1] == "CLICK":
        m.click()

    if args[1] == "MOVE":
        m.move(args[2], args[3])

    if args[1] == "DRAG":
        m.drag(args[2], args[3], args[4])