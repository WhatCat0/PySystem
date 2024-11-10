import System as sys

File = sys.registry.filestart
if sys.os.path.isfile(File):
    if sys.registry.sfm == 'tpv':
        exec(open(File).read())
    elif sys.registry.sfm == 'apv':
        sys.os.system('python ' + File)
else:
    print('Error: file not found')