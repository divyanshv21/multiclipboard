# Clipboard manager with command line functionality

Let's say you have the unenviable chore of filling out a bunch of forms in some software or on a website. You can avoid repeatedly typing the same thing by using the clipboard. However, the clipboard can only hold one item at a time. Copying and pasting from multiple sources requires repeatedly highlighting and copying the same little subset of text.

Python allows you to easily create programs that can store and organize large amounts of text. Given that "mcb" is easier to type than "multiclipboard," we've decided to shorten the file name for this "multiclipboard" to mcb.pyw. Python will not open a Terminal window to run this program because of the.pyw extension.  

Each selection copied to the clipboard will be saved in the database with a keyword. To save the current clipboard contents with the keyword "spam," for instance, execute py mcb.pyw save spam. Pasting the results of py mcb.pyw spam into the clipboard will reload the previously copied text. To copy a whole list of keywords to the clipboard in case the user forgets what they are, they need only type py mcb.pyw list.

To run the `mcb.pyw` program, follow these steps:

1. **Save the Script**: First, save the Python script with the name `mcb.pyw` on your computer. Ensure that it's saved in a directory where you have write permissions.

2. **Open a Terminal or Command Prompt**:
   - On Windows, press `Win + R`, type `cmd`, and press Enter.
   - On macOS or Linux, open the Terminal.

3. **Navigate to the Directory**: Use the `cd` command to navigate to the directory where you saved the `mcb.pyw` script.

4. **Run the Script**:

   - To save clipboard content to a keyword, use the following command:
     ```
     py.exe mcb.pyw save <keyword>
     ```
     Replace `<keyword>` with the keyword you want to use.

   - To load clipboard content associated with a keyword, use the following command:
     ```
     py.exe mcb.pyw <keyword>
     ```
     Replace `<keyword>` with the keyword you want to load.

   - To list all keywords in the shelf, use the following command:
     ```
     py.exe mcb.pyw list
     ```

5. **Press Enter**: After entering the appropriate command, press Enter to run the script.

The script will perform the specified action based on the command-line arguments you provide. It will either save clipboard content to a keyword, load clipboard content associated with a keyword, or list all keywords in the shelf.

Ensure that you have the necessary Python packages (`shelve` and `pyperclip`) installed for the script to work correctly. You may need to replace `py.exe` with `python3` if you're using a different Python interpreter.
