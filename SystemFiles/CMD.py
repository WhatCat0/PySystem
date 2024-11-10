import System

while System.registry.runingCMD:
    cmd = input(System.os.getcwd() + '\\')
    match cmd.split():
        case ["quit"]:
            System.runingCMD = False
            System.runing = False
            exit(0)
        case ['pc', command]:
            exec(command)
        case ['cd', directory]:
            print(System.directores.cd(directory))
        case ['dir']:
            System.directores.PrintListDir()
        case ['mkdir', file]:
            print(System.directores.createDirectory(file))
        case ['delfile', file]:
            print(System.files.deleteFile(file))
        case ['deldir', directory]:
            print(System.directores.delDirectory(directory))
        case ['mkfile', name]:
            System.files.createFile(name)
        case ['install', name]:
            System.os.system(f'pip install {name}')
        case [any]:
            if System.os.path.isfile(cmd):
                System.files.startFile(cmd)
            else:
                print('Error: command not found')