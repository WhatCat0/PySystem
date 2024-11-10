File = registry.filestart # type: ignore
if os.path.isfile(File): # type: ignore
    if registry.sfm == 'tpv': # type: ignore
        exec(open(File).read())
    elif registry.sfm == 'apv': # type: ignore
        os.system('python ' + File) # type: ignore
else:
    print('Error: file not found')