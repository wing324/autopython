**SCRIPT NAME**  

Create Bigdata For MySQL  

**SCRIPT USAGE**  

```
[root@wing python]# python create_bigdata_for_MySQL.py 
please input the number you want to insert : 10000
please input the min value of auto_increment : 0
please input the length of random string : 8
# This script requires three interactions
# The first interaction to get the number of data you want to insert
# The second interaction to get the minimum values of auto_increment column(you must do it ,regardless of your table including auto_increment column,if your table lack of auto increment column,ths value without any influence)
# The last interaction to get the length of the string you want to insert for string type
```

**Notes**  

1. If you insert a large amount of data,you should tempprarily increase the global parameter of max_allowed_packet.Otherwise,MySQL will report the following stutiation:  

   https://github.com/wing324/AutoPython/issues/1
