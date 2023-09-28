# multiclipboard

Let's say you have the unenviable chore of filling out a bunch of forms in some software or on a website. You can avoid repeatedly typing the same thing by using the clipboard. However, the clipboard can only hold one item at a time. Copying and pasting from multiple sources requires repeatedly highlighting and copying the same little subset of text.

Python allows you to easily create programs that can store and organize large amounts of text. Given that "mcb" is easier to type than "multiclipboard," we've decided to shorten the file name for this "multiclipboard" to mcb.pyw. Python will not open a Terminal window to run this program because of the.pyw extension.  

Each selection copied to the clipboard will be saved in the database with a keyword. To save the current clipboard contents with the keyword "spam," for instance, execute py mcb.pyw save spam. Pasting the results of py mcb.pyw spam into the clipboard will reload the previously copied text. To copy a whole list of keywords to the clipboard in case the user forgets what they are, they need only type py mcb.pyw list.

