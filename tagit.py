# create tags files for python3 at dir and its children if any
import os


# gloabal variables
# first, collect all the dir and child dirs
# use os.walk()
total = list(os.walk(os.getcwd()))
dirs = []
files = []

def setup():
    # tri: (dir,child_dir,file)
    for tri in total:
        dirs.append(tri[0])
        files.append(tri[2])

def walk_and_create_tags(counts=True):
    # then loop thru these dirs to create tag
    # simple for-loop
    # and single var s=""
    cnt = 0 # number of files for debug
    for d, lis in zip(dirs,files):
        s = ""
        for f in lis:
            if f.count(".") == 1:
                if ".py" == f[-3:]:
                    print("passed", f)
                    s += f + " "
                    cnt += 1
        os.chdir(d)
        os.system("tagitpy.bat " + s)
    if counts:
        print("\nparse %d files\n" % cnt)

def main():
    setup()
    walk_and_create_tags()


if __name__=="__main__":
    main()



