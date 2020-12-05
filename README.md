# TextEncodingConverter 文本编码转换

### Require: python 3 chardet

## How to use:

1.Download Converter.py

2.Put the text files and Converter.py in the same folder 

3.Set two parameters(start from line 27)

```python
(1)fileType:
	The file type you want to convert
	Example: 
    	fileType = ".txt" 
    	fileType = ".bat"
    
(2)targetEncoding:
    The text encoding you want to convert to 
    There is no need to input source file encode,this program will automatically detect that.
    Example:
        targetEncoding = "utf-8"
        targetEncoding = "shift-jis"
        ......
```

4.run

start the powershell or cmd in the folder and input:

```shell
python Converter.py
```

5.finish

A new folder named "ConvertRst" will be created and the result file will be put in it.

6.be careful that when you want to convert again files in the same folder, please delete the old "ConvertRst" folder .

# 中文版：

### 需求：python 3 chardet

## 使用方法：

1.下载Converter.py这个文件

2.把Converter.py和需要转码的文本文件（可以放多个，数量不限，保证后缀名相同即可）放在同一个文件夹下

3.设置两个参数（后缀名和目标编码），从27行开始

```python
(1)fileType:
	文件的后缀名
	例子: 
    	fileType = ".txt" 
    	fileType = ".bat"
    
(2)targetEncoding:
    要转换成的编码
    不需要输入源文件的编码，程序会自动检测的。
    例子:
        targetEncoding = "utf-8"
        targetEncoding = "shift-jis"
        ......
```

4.在当前文件夹（就是放源文件和Converter.py的文件夹）下打开cmd或者powershell（直接在地址栏里输cmd）运行以下代码：

```python
python Converter.py
```

5.程序会创建一个叫"ConvertRst"的文件夹，转码后的文件会存放在这里

6.注意：如果还是在这个文件夹里，想要再次转码文件，请删除之前的"ConvertRst"文件夹，不然会报错。
