import os
def fetch(url,filename=""):
    import requests
    #import hashlib
    #import tempfile
    #fp = os.path.join(tempfile.gettempdir(), hashlib.md5(
    #    url.encode('utf-8')).hexdigest())
    if len(filename) == 0:
        print("filename not assginged, returned")
        return

    fp = "./" + filename
    if os.path.isfile(fp):
        with open(fp, "rb") as f:
            dat = f.read()

    else:
        dat = requests.get(url).content
        # important trick here to create a .tmp file
        with open(fp+".tmp", "wb") as f:
            f.write(dat)
        os.rename(fp+".tmp", fp)

    return fp[2:]
    #return dat

import sys

# default setting
filename = fetch("https://raw.githubusercontent.com/jserv/linux-list/master/include/list.h","linux_list.c")
if len(sys.argv) == 2:
    if sys.argv[1] == "y":
        os.system("vim " + filename)
# end default setting

elif len(sys.argv) == 3:
    os.system("vim " + fetch(sys.argv[1],sys.argv[2])) 


