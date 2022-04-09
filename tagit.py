# just write the whole thing to the topest dir
import os


# gloabal variables
# first, collect all the dir and child dirs
total = list(os.walk(os.getcwd()))
dirs = []
files = []

def setup():
    # triple: (dir,child_dir,file)
    for tri in total:
        dirs.append(tri[0])
        files.append(tri[2])

def walk_and_create_tags(counts=True):
    # number of files for debug
    cnt = 0
    # loop thru all the dirs for .py files
    #  and store them in "s" variable
    s = ""
    for d, lis in zip(dirs,files):
        for f in lis:
            if f.count(".") == 1:
                if ".py" == f[-3:]:
                    print("passed", f)
                    # needs to add base path
                    # chr(92) is "\"
                    s += d +chr(92) + f + " "
                    cnt += 1
        # to avoid "too long cmd line problem"
        if cnt % 50 == 49:
            os.system("tagitpy.bat " + s)
            # reset s
            s = ""
    # on last time, convert the remained files
    os.system("tagitpy.bat " + s)
    if counts:
        print("\nparse %d files\n" % cnt)

def main():
    setup()
    walk_and_create_tags()


if __name__=="__main__":
    main()



