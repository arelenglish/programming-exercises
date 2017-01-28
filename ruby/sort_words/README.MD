Given a list of words (see the included 'words.txt' list), generate two output files, 'uniques' and 'fullwords'. The 'uniques' output file should contain every sequence of four letters that appears in exactly one word of the dictionary, with one sequence of four letters per line, alphabetized. The 'fullwords' file should contain the corresponding full, original words that contain the sequences in the 'uniques' file, in the same order, again one per line.

This code should finish running in under 2 seconds.

An example:

Say this is your dictionary:
bicycle
book
for
recycle


'uniques' would contain:
bicy
book
ecyc
icyc
recy


and 'fullwords' would have:
bicycle
book
recycle
bicycle
recycle


'cycl' and 'ycle' wouldn't show up in 'uniques', because they each appear in more than one word.

If anything in these instructions seems ambiguous, make the best decision you can, and explain your decision. Please write in Python or explain why you chose not to.

# Solution

The solution is in the `solution.rb` file. To run it open `irb`, and follow these instructions:
  * run `load 'solution.rb'`
  * run `w = WordFinder.new`
  * run `w.run`

  Your results will be printed in the `uniques.txt` file and the `fullwords.txt` file. You'll be able to find those files in the root directory with `solution.rb`
