# Welcome to Rolodex

Rolodex generates a formatted and organized JSON rolodex or address book
from raw address data. 

Rolodex conviently comes with example data (`data.in`) and file of the expected
output: (`json.out`).

Quickstart: `$ python3 back_end_rolodex.py data.in`

####Formats

Rolodex currently supports three formats of address input:

* Lastname, Firstname, (703)-742-0996, Blue, 10013 
* Firstname Lastname, Red, 11237, 703 955 0373 
* Firstname, Lastname, 10013, 646 111 0101, Green 

####Using Rolodex

######From Bash:

Create a file of addresses putting one address per line. Addresses can be formatted 
in any of the supported formats. Then, simply cd into the rolodex directory and type 
`$ python3 back_end_rolodex.py data.in`, or whatever your input file is called. 
Your json.out file will automatically be created for you in the current directory.

Optionally, you can also build this program by running `chmod +x back_end_rolodex.py`
then simply run your program like this `$ ./back_end_rolodex.py data.in` 

From REPL

Import the `rolodex` function from this file: `from back_end_rolodex import rolodex` 
then simply call the `rolodex` function with your data file, like this: 
`rolodex('./data.in')`

####Testing Rolodex

Rolodex is fully tested. To run the tests, run `$ python3 back_end_rolodex_tests.py`
from the terminal.
