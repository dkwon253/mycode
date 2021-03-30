#!/usr/bin/env python3

# import statement to move files
import shutil
import os

# call on the import statement
os.chdir("/home/student/mycode/")


shutil.move("raynor.obj", "ceph_storage/")


xname = input("What is the new name for kerrigan.obj?")

# The following line will rename a file
shutil.move("ceph_storage/kerrigan.obj", "ceph_storage/" + xname)

