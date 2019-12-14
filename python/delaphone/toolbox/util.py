from colorama import Fore, Style

def ask_yesno(prompt):
    while True:
        ans = input("{}{} (yes/no)?{} ".format(
            Style.BRIGHT, prompt, Style.RESET_ALL)).strip().lower()
        if ans in ('n', 'no'):
            return False
        elif ans in ('y', 'yes'):
            return True
        else:
            print("Unrecognized answer. Try again")
