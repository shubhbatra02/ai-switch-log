from pathlib import Path
with open("day5/sample.log","a",encoding="utf-8") as f:
    f.write("INFO: listener started\n")
    f.write("WARNING: tablespace 90% full\n")
    f.write("ERROR: ORA-00060 deadlock detected\n")
    f.write("INFO: user login successful\n")