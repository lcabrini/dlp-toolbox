def ask_yesno(prompt):
    while True:
        ans = input("{} (yes/no)? ".format(prompt)).strip().lower()
        if ans in ('n', 'no'):
            return False
        elif ans in ('y', 'yes'):
            return True
        else:
            print("Unrecognized answer. Try again")

