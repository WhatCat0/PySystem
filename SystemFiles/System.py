import codecs, os, sys, shutil, json, cmd
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
    def createFile(file, info):
        with open(file, 'w', encoding = "utf-8") as f:
            f.write(info)
    def deleteFile(file):
        if os.path.isfile(file):
            os.remove(file)
            return 'Done!'
        else:
            return 'Error: file not found'  
    def startFile(file):
        other.filestart = file
        directores.cd('ProgramFiles/OFA')
        f = codecs.open(f'{os.getcwd()}/{os.path.splitext(file)[1]}/{other.getRegistry()["FOF"][os.path.splitext(file)[1]]}', "r", "utf-8" )
        exec(f.read())
        f.close()
class info:
    pythonversion = sys.version
    platform = sys.platform
class other:
    filestart = None
    runing = True
    runingCMD = True
    def getRegistry():
        with open('SystemFiles/registry.json', 'r') as f:
            return json.load(f.read)
print("Welcome to PySystem v7.0 beta 2!")
print(info.pythonversion + ' on '
    +  info.platform )

if __name__ == '__main__':
    files
    directores
    info   
    other