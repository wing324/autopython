**SCRIPT NAME**  

RENAME MySQL DATABASE  



**SCRIPT USAGE**  

- Simplest operation(and recommanded),rename database wing to test  

  ```
  [root@wing python]# python rename_tables.py -u root -H 127.0.0.1 -P 3306 --ask-pass -o wing -n test
  -- Connecting to MySQL......
  Please input your MySQL password:
  -- get tables from old database......
  -- rename database ......
  Total:4 tables are renamed
  -- Complete!
  ```


- Drop old database and create new database operation(not recommanded),rename databasae test to wing(test is old database,wing is new database)  

  ```
  [root@wing python]# python rename_tables.py -u root -H 127.0.0.1 -P 3306 --ask-pass -o test -n wing -c -d
  -- Connecting to MySQL......
  Please input your MySQL password:
  The wing database exists!
  -- get tables from old database......
  -- rename database ......
  Total:4 tables are renamed
  -- Drop old database......
  -- Complete!
  ```

**Notes**  

- This script without doing any check operation before rename database.So you need to do security checks before rename database.Otherwise, it is possiblly to cause data inconsistency or other problems.  
- Before using this script,please make sure that the rename database operation is required.
