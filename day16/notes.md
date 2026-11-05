 Question: What does ORA-01555 mean? Answer in two sentences.
   Correct: Snapshot too old. A long-running query needed undo data that was already overwritten.
  RUN 1 (no system message):
ORA-01555 is a database error in Oracle, indicating that a partitioned table or index has been created with a space that does not allow the data to be written. This error typically occurs when the table or index is created with a space allocation that is too small, causing data to be rejected or not written to the table.

RUN 2 (with system message):
ORA-01555 is an Oracle error that indicates the database is running out of space to hold the redo log, which is used to recover the database in case of a failure. The error typically occurs when the size of the redo log is not sufficient to accommodate the required space for a particular operation, such as a DDL statement.
shubhambatra@KeertiShubham ai-switch-log-1 % /usr/local/bin/python3
 /Users/shubhambatra/Desktop/ai-switch-log-1/day16/ask.py
RUN 1 (no system message):
ORA-01555 is a database error that occurs when the Oracle databaseis unable to reclaim space from a table or index due to a deadlocksituation. This error typically occurs when a table or index has been locked by a transaction, and the database is unable to release the lock, resulting in a deadlock that prevents the database from reclaiming space.

RUN 2 (with system message):
ORA-01555 is an error message that indicates a constraint or indexissue, typically due to an invalid or corrupted index or constraint, causing the database to fail during maintenance operations such as drop or rebuild. This error often occurs when a dependent object(e.g., a view or procedure) references a dropped or invalid object, preventing the database from completing the operation.
   Conclusion: a prompt can't add missing knowledge. The fix is to give the model the right text (RAG).



   Q: What does ORA-00600 mean?
Model: llama3.1:8b
Verdict: partly correct (right gist, missed first argument, alert log, ADRCI)


## Test: fake error code
Q: What does ORA-99999 mean?
Model: llama3.1:8b
Answer: invented a "generic fatal error" explanation
Verdict: hallucination (no such documented code, model never said it didn't know)
System message on: <invented / admitted not knowing>
System message off: <invented / admitted not knowing>


The RAG assistant has to do three things:

Answer only from retrieved text, and cite which note it came from.
Say “not found in the knowledge base” when retrieval returns nothing relevant.
Pass your test cases. ORA-99999 should produce “not found”, and ORA-01555 should produce an answer that matches your note.