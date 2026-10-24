Oracle Alert Log Error Summarizer

A small Python tool that reads an Oracle alert log, counts how many times each ORA- error code appears, and prints a summary sorted by frequency (highest first).

What it does
Reads a log file line by line.
Finds lines containing ORA-, even when a timestamp or other text comes before the code.
Extracts the error code (for example ORA-01555) and counts each one in a dictionary.
Prints the counts sorted from most to least frequent.
Shows a friendly message if the log file is missing, instead of crashing.
How to run
Put your log file next to the script and name it sample.log (or change the filename in the script).
Run:
python3 readora.py