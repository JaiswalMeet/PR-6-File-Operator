import os
from datetime import datetime

class MyJournal:
    def __init__(self):
        self.filename = "journal.txt"

    def write_entry(self, data):
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "a") as f:
            f.write(f"[{dt}] {data}\n")
        print("Entry saved")

    def read_entries(self):
        try:
            with open(self.filename, "r") as f:
                print(f.read())
        except:
            print("No entries yet.")

    def clear_journal(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print("Journal cleared")

j = MyJournal()

while True:
    print("\n1. Add Entry\n2. Read Journal\n3. Delete Journal\n4. Exit")
    c = input("Option: ")

    if c == '1':
        j.write_entry(input("Type your entry: "))
    elif c == '2':
        j.read_entries()
    elif c == '3':
        j.clear_journal()
    elif c == '4':
        break