```
Antlr4使用过程:
1、创建语法文件
   按照业务要求定义语法文件.g4
2、生成语法解析代码 
   2.1使用antlr4生产相关代码
       java -jar ~/work/antlr-4.7.1-complete.jar -visitor -Dlanguage=Python2 EdataLr.g4
   2.2编写解析逻辑
3、调用/使用
   python3.7 edata.py t.txt 
```
