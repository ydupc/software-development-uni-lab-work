while True:
    ans = input("Are you sure you want to delete the record? (y/n) ").strip().lower()
    if ans in ("y", "n"):
        break
    print("Sorry, you must answer 'y' or 'n'.")
print("Record was deleted." if ans == "y" else "Record was not deleted.")
