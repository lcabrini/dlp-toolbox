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

def can_sudo():
    # TODO: implement this
    return True

def check_sudo_password(sudo_password):
    # TODO: implement this
    return True

def generate_password():
    # This may change later.
    uc = string.ascii_uppercase
    pw = ''.join(random.choice(uc) for i in range(3))
    pw += "-"
    pw += ''.join(random.choice(string.digits) for i in range(6))
    return pw
