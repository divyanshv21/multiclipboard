import shelve
import pyperclip
import sys

def save_to_clipboard(keyword):
    mcbShelf[keyword] = pyperclip.paste()

def load_from_clipboard(keyword):
    if keyword in mcbShelf:
        pyperclip.copy(mcbShelf[keyword])
    else:
        print(f"No entry found for '{keyword}'.")

def delete_keyword(keyword):
    if keyword in mcbShelf:
        del mcbShelf[keyword]
        print(f"Deleted '{keyword}' entry.")
    else:
        print(f"No entry found for '{keyword}'.")

def delete_all_keywords():
    mcbShelf.clear()
    print("All entries deleted.")

if len(sys.argv) == 3:
    mcbShelf = shelve.open('mcb')
    command = sys.argv[1].lower()
    keyword = sys.argv[2]

    if command == 'save':
        save_to_clipboard(keyword)
    elif command == 'load':
        load_from_clipboard(keyword)
    elif command == 'delete':
        delete_keyword(keyword)
    else:
        print("Invalid command. Use 'save', 'load', 'delete', or 'deleteall'.")
else:
    print("Usage: python mcb.pyw <command> <keyword>")
    print("Commands: save, load, delete, deleteall")

if 'mcbShelf' in locals():
    mcbShelf.close()
