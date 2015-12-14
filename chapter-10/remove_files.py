"""
Write a script remove_files.py that will look in the chapter 10 practice files folder named
“little pics” as well all of its subfolders. The script should use os.remove() to delete any
JPG file found in any of these folders if the file is less than 2 Kb (2,000 bytes) in size.
You can supply the os.path.getsize() function with a full file path to return the file’s size
in bytes. Check the contents of the folders before running your script to make sure that you
delete the correct files; you should only end up removing the files named “to be deleted.jpg”
and “definitely has to go.jpg” - although you should only use the file extensions and file sizes
to determine this.
If you mess up and delete the wrong files, there is a folder named “backup” that contains an
exact copy of the “little pics” folder and all its contents so that you can copy these contents
back and try again.
"""
import os
my_path = "/home/milco/real-python/real-python-1/chapter-10/little pics/"

for current_folder, subfolders, file_names in os.walk(my_path):
    for file_name in file_names:
        fullname = os.path.join(current_folder, file_name)
        if fullname.lower()[-4:] == ".jpg" and os.path.getsize(fullname) < 2000:
            print "File has to go: "  + fullname
            os.remove(fullname)
        else:
            print "File OK: "  + fullname
            
