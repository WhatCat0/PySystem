if os.path.isfile(registry.filestart): # type: ignore
    with open(registry.filestart, "r", encoding = "utf-8") as f: # type: ignore
        info = f.read()
        print(info)
else:
    print('Error: file not found')