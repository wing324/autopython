**脚本名称**  

Create Bigdata For MySQL  

**脚本目的**  

在MySQL工作中往往存在许多对知识点的验证，比如SQL语句的优化，经常需要一张很大的表才能正在体会到SQL优化的优点，那么这个大数据的表怎么来呢？手动INSERT INTO的方式已经是上古时代的方式了。现在我们需要解放自己，让机器来替我们工作。于是就有了这个脚本的诞生。  

**脚本使用**  

```
[root@wing python]# python create_bigdata_for_MySQL.py 
please input the number you want to insert : 10000
please input the min value of auto_increment : 0
please input the length of random string : 8
# 整个脚本中需要输入三次
# 第一次是输入你想要插入多少条数据量
# 第二次是输入auto_increment列的最小值（不管你的表结构中是否存在auto increment列，都需要进行输入，当然，如果表结构中不存在auto increment列，那么该值不产生作用）
# 第三次是输入对于字符串类型来说你想要插入的字符串长度
```

**注意事项**  

1. 对于插入大量数据时，注意适当的增大max_allowed_pocket参数，否则会出现下面的情况：  

   https://github.com/wing324/AutoPython/issues/1  
