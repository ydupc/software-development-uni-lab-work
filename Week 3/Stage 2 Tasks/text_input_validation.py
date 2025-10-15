VALID_YES = {"y","yes"}
VALID_NO  = {"n","no"}
def ask_confirm(prompt="Are you sure you want to delete the record? (y/n) "):
    while True:
        ans = input(prompt).strip().lower()
        if ans in VALID_YES: return True
        if ans in VALID_NO:  return False
        print("Sorry, you must answer 'y' or 'n'.")
if __name__ == "__main__":
    confirmed = ask_confirm()
    print("Record was deleted." if confirmed else "Record was not deleted.")
