import codecs
import os, sys, shutil, CMD

class directores:
    def GetListDir():
        return os.listdir()
    def PrintListDir():
        for item in directores.GetListDir():
            print(item)
    def cd(directory):
        try:
            os.chdir(directory)
        except:
            return f'Error: {sys.exc_info()}'
        finally:
            os.chdir(os.getcwd())
            return 'Done !'
    def createDirectory(name):
        os.mkdir(name)
        return f'Directory {name} created!'
    def delDirectory(directory):
        if os.path.isdir(directory):
            shutil.rmtree(directory)
            return 'Done!'
        else:
            return 'Error: directory not found'
class files:
    def createFile(file):
        open(file, "x", encoding = "utf-8")
    def deleteFile(file):
        if os.path.isfile(file):
            os.remove(file)
            return 'Done!'
        else:
            return 'Error: file not found'  
    def startFile(file):
        registry.filestart = file
        indexFOF = 2
        match os.path.splitext(file)[1]:
            case [".json"]:
                indexFOF = 0
            case [".py"]:
                indexFOF = 1
            case [".txt"]:
                indexFOF = 2
        directores.cd('ProgramFiles/OFA')
        f = codecs.open(f'{os.getcwd()}/{os.path.splitext(file)[1]}/{registry.FOF[indexFOF]}', "r", "utf-8" )
        exec(f.read())
        f.close()
class info:
    pythonversion = sys.version
    platform = sys.platform
class registry:
    FOF = ['defalt.py', 'defalt.py', 'defalt.py']
    filestart = None
    runing = True
    runingCMD = True

print("Welcome to PythonSystem build 7(beta)!")
print(info.pythonversion + ' on '
    +  info.platform )

if __name__ == '__main__':
    files
    directores
    info   
    registry