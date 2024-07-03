# IS218 Midterm 2024
## Welcome to my midterm submission!
The goal of this repository/assignment is to setup a command-line interface centered around REPL. Create a flexible plugin system that allows easy integration of new commands and features that automatically show up when typing the "Menu" command in the command-line. Use Pandas to manage saving calculator history and giving the user a robust set of features to manipulate the data. Implement professional logging practices, or at least in this case, enough to hope to not lose points :). I did my best with version history and control by seperating branches based on what core functionaility I needed to add and commits based on what exactly I did to check off a mark in that functionaility. Pytest should be giving no critical errors and Pylint tells me everything is in order except for some things I needed to add to the disable list in .pylintrc file.

## Setup Instructions
1. Clone the repository
```
git clone git@github.com:mjedryczka/midterm.git
```

2. Create a Python virtual environment andd enter it
```
virtualenv venv
source venv/bin/activate
```

3. Install python dependencies
```
pip install -r requirements.txt
```

4. Run the program
```
python3 main.py
```

## Example Usage
A command list that shows every type of command available can be shown by typing `menu`. Commands do not need to be case-sensitive.

### Arithmetic
Entering the math commands in this format `<operation> <numberA> <numberB>` allows for math operations to be created, added to a history, and outputed straight to the command-line. Available math commands are as follows `add`, `subtract`, `multiply`, `divide`.

### History
Whenever you run a math command, it stores that information with the result in memory. You can access this history by running the `history_print` command. This prints out the operations into the command-line. If you'd only want to print the last calculation, run `history_print_latest`. And to search and print operations from memory, run `history_get_by_operation`.

### Save File
While having information stored in memory is fun and all, but storing the information for later has its uses. To save the calculations stored in memory use `save_make`, to add a save file to the running program's memory, run `save_load`. To delete the newest or oldest entry in the save file, assumging it exists, run `save_delete_newest` or `save_delete_oldest` respectively.

### Configuration
Currently there isn't much that the user can configure. Only thing avaible is to change the destination for saving the calculation history as well as the name. The default value if none is set is "calculations.csv".

### Programming Design Patterns
One major architectural decision is the heavy use of OOP principles. It's one of the reasons why there are so many files and why they work properly. Every class has it's own file and does it's assigned role. Only to be extended, not heavily modified. And files shouldn't import libraries and methods that they do not need to save a few lines and to add focus on the code. Another way I saved space is to try to limit repetition in the code wherever possible. Just about the entirity of the [Calculator Folder](app/calculator) is OOP centered.
Logging is one of those things I'd never need for my projects. A simple print statement to make sure things are working then deleting it. But that's a death sentence, same with not leaving comments. Eventually when the prorgams large enough and people are working on it, it becomes absolutely important. Hence why I made sure to addd logging to every file related to the process of running the program. Using INFO to display print results, WARNING to point out potential problems like a missing .env file, missing save_file_dest variable, or an attempt at [division](app/plugins/divide/__init__.py). Also CRITICAL whenver something would break when it shouldn't break.
On the note of things breaking when they shouldn't, I've placed try-excepts on every [Plugin](app/plugins) and every actions that has a risk of failing, like taking use input from the command-line or a math operation from the calculator side. I emphasize calculator side as to clarify that I utilize the proper classes and dnot just skip and use directly from the operations file.

### Youtube Video
https://youtu.be/kUIj4uBtCTY