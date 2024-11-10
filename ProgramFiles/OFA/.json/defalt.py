import System as sys

if sys.os.path.isfile(sys.registry.filestart):
    with open(sys.registry.filestart, "r", encoding = "utf-8") as f:
        info = f.read()
        print(info)
else:
    print('Error: file not found')