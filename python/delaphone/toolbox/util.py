from getpass import getpass
from colorama import Fore, Style

def ask_yesno(prompt):
    while True:
        prompt = build_prompt(prompt, "?", ("yes", "no"))
        ans = input(prompt).strip().lower()
        if ans in ('n', 'no'):
            return False
        elif ans in ('y', 'yes'):
            return True
        else:
            print("Unrecognized answer. Try again")

def inputpw(prompt="Password"):
    prompt = build_prompt(prompt)
    return getpass(prompt)

def inputs(prompt):
    prompt = build_prompt(prompt)
    return input(prompt)

def build_prompt(prompt, punctuation=":", options=()):
    p = "{}{}{}".format(Style.BRIGHT, prompt, Style.RESET_ALL)
    o = ["{}{}{}".format(Fore.GREEN, opt, Fore.RESET) for opt in options]
    if len(options) == 2:
        p += " ({})".format('/'.join(o))
    elif len(options) > 2:
        p += " ({})".format(', '.join(o))
    p += "{} ".format(punctuation)
         
    return p
