from pathlib import Path

with open("day6/sample.log","w",encoding="utf-8") as f:
    f.write("Thu Oct 22 10:01:11 2026\n")
    f.write("Starting ORACLE instance (normal)\n")
    f.write("Thu Oct 22 10:01:11 2026 ORA-00600: internal error code, arguments: [kcbz_check_objd_typ]\n")
    f.write("Thread 1 advanced to log sequence 4521\n")
    f.write("Thu Oct 22 10:01:11 2026 ORA-01555: snapshot too old: rollback segment number 4 too small\n")
    f.write("Thu Oct 22 10:01:11 2026 ORA-00060: deadlock detected while waiting for resource\n")
    f.write("Completed: ALTER DATABASE OPEN\n")
    f.write("Thu Oct 22 10:01:11 2026 ORA-01555: snapshot too old: rollback segment number 7 too small\n")
    f.write("Thu Oct 22 10:01:11 2026 ORA-00600: internal error code, arguments: [kdsgrp1]\n")
    f.write("ORA-01555: snapshot too old: rollback segment number 4 too small\n")
    f.write("INFO: listener started\n")
    f.write("WARNING: tablespace 90% full\n")
    f.write("Thu Oct 22 10:01:11 2026 ORA-00060: deadlock detected\n")
    f.write("INFO: user login successful\n")
