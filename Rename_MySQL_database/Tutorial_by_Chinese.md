**脚本名称：**  
MySQL数据库重命名  

**脚本目的：**  
有时候在数据库创建时，由于一时大意，不小心写错数据库名称，当该数据库下没有数据时，重命名数据库没什么大问题，可以通过DROP DATABASE和CREATE DATABASE进行数据库重新创建。万一该数据库下有很多表，例如有个成百上千的表，MySQL又没有直接提供RENAME DATABASE的语句，如果仅仅是通过SQL语句来重命名数据库是有点麻烦的。所以有了这个危险的工具的诞生。为什么说它是危险的。因为数据库的重命名，必须是非常谨慎的操作。  

**脚本使用：**  
- 最简单的操作（也是最推荐的），将wing数据库名称重命名为test数据库名称
```
[root@wing python]# python rename_tables.py -u root -H 127.0.0.1 -P 3306 --ask-pass -o wing -n test
-- Connecting to MySQL......
Please input your MySQL password:
-- get tables from old database......
-- rename database ......
Total:4 tables are renamed
-- Complete!
```
- 携带删除旧数据库，添加新数据库的操作（最不推荐的），将test数据库名称重命名为wing数据库名称，test为旧数据库，wing为新数据库
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

**注意事项：**  
1. 该脚本中在rename database之前没有做任何的检查操作，例如是否有程序正在使用需要重命名的数据库，所以需要使用人对该数据库做安全检查。否则，有造成数据不一致以及其他问题的可能性。  
2. 使用该脚本前，确定一定以及肯定是需要rename database操作的。
