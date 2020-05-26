import os
import chardet


def startConvert(fileType, targetEncoding):
    filePath = os.getcwd()
    fileList = os.listdir(filePath)
    os.mkdir("ConvertRst")

    lenOfExt = len(fileType)
    for filename in fileList:
        if filename[-lenOfExt:] == fileType:
            encode = chardet.detect(open(filename, "rb").read())
            sourceFile = open(filename, "r", encoding=encode["encoding"])
            targetFile = open(filePath + "/ConvertRst/" + filename, "a", encoding=targetEncoding)
            ctx = sourceFile.read()
            targetFile.write(ctx)
            sourceFile.close()
            targetFile.close()
            print("Filename:", filename)
            print("Encoding:", encode["encoding"])
            print("Language:", encode["language"])
            print("Confidence:", encode["confidence"])


if __name__ == '__main__':
    #########settings#########
    '''
    fileType:
    The file type you want to convert
    Example: 
        fileType = ".txt" 
        fileType = ".bat"
        ......
    '''
    fileType = ".txt"
    '''
    targetEncoding:
    The text encoding you want to convert to 
    There is no need to input source file encode,this program will automatically detect that.
    Example:
        targetEncoding = "utf-8"
        targetEncoding = "shift-jis"
        ......
    '''
    targetEncoding = "utf-8"
    #########Run#########
    startConvert(fileType, targetEncoding)
    input("PRESS ANY KET TO EXIT")
