# write all the tags file at topest dir only

import sys, re, os

# take advantage of original ptags.py script
# start of ptags.py
tags = []    # Modified global variable!
"""
def main():
    args = sys.argv[1:]
    for filename in args:
        treat_file(filename)
    if tags:
        fp = open('tags', 'w')
        tags.sort()
        for s in tags: fp.write(s)
"""

expr = r'^[ \t]*(def|class)[ \t]+([a-zA-Z0-9_]+)[ \t]*[:\(]'
matcher = re.compile(expr)

def treat_file(filename):
    try:
        fp = open(filename, 'r')
    except:
        sys.stderr.write('Cannot open %s\n' % filename)
        return
    base = os.path.basename(filename)
    if base[-3:] == '.py':
        base = base[:-3]
    s = base + '\t' + filename + '\t' + '1\n'
    tags.append(s)
    while 1:
        line = fp.readline()
        if not line:
            break
        m = matcher.match(line)
        if m:
            content = m.group(0)
            name = m.group(2)
            s = name + '\t' + filename + '\t/^' + content + '/\n'
            tags.append(s)

## end of ptags.py

# first, get all the child dir
root = os.getcwd() # a string
totaldir = list(os.walk(root))
totalchild = [ele[0] for ele in totaldir]
totalfile = [ele[2] for ele in totaldir]


fullfile = [] # full file list with basename + filename
def concat_dirs():
    #s = ""
    cnt = 0
    for d, fs in zip(totalchild,totalfile):
        for f in fs:
            if ".py" == f[-3:]:
                if len(d[(len(root)+1):]) > 0:
                    #s += d[(len(root)+1):] + chr(92) + f + " "
                    fullfile.append(d[(len(root)+1):] + chr(92) + f + " ")
                else:
                    #s += d[(len(root)+1):] + f + " "
                    fullfile.append(d[(len(root)+1):] + f + " ")
                cnt += 1
    print("processed %d files" % cnt)
    #return s


def main():

    concat_dirs()

    for f in fullfile:
        # process and append all the files from all dirs to tags list
        treat_file(f)

    if tags: # if tags list is not emtpy
        fp = open('tags', 'w')
        tags.sort()
        for s in tags: fp.write(s)


if __name__=="__main__":
    main()




