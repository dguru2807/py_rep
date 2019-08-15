import os
import glob

# set the path where the source  and destination files are available
sourcepath = "D:\Projects\PY_SRC"
destpath = "D:\Projects\PY_DEST"

# set the delimiter
delimiter = ","

# loop through only the .txt files present in your folder
for filename in glob.glob(os.path.join(sourcepath, '*.txt')):

    #  open the source file
    srcfile = open(filename, 'r')

    # loop through each line of the source file
    for i in srcfile:
        fields = i.split(delimiter)

        # define the destination file name
        destfilename = os.path.join(destpath, fields[1]+ ".txt")

        # appending the destination path
        destfile = open(destfilename, "a+")
        destfile.write(i)
        destfile.close()

    srcfile.close()


