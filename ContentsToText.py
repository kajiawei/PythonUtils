#!/usr/bin/env python

import sys
import os


def list_dir_contents(contents, relative_path):    
    #raw_input('paused')

    abs_path = rootdir_path + '\\' + relative_path
    print 'looking in ' + abs_path
    print 'relative path: ' + relative_path

    child_dirs = [ d for d in os.listdir(abs_path) if os.path.isdir(os.path.join(abs_path, d)) ]
    files = [ f for f in os.listdir(abs_path) if os.path.isfile(os.path.join(abs_path, f)) ]

    if len(child_dirs) == 0 and len(files) == 0:
        print 'Empty dir...'
        contents += rootdir_name + '\\' + relative_path + '\n'
        return contents

    for folder_name in child_dirs:
        contents = list_dir_contents(contents, relative_path + "\\" + folder_name)

    if len(files) > 0:
        print 'Adding files in ' + relative_path
        for file_name in files:
            contents += rootdir_name + '\\' + relative_path + '\\' + file_name + '\n'

    return contents

print 'args: '
for argument in sys.argv:
    print argument + ' '
print '\n'

if len(sys.argv) != 2:
    error_str = 'Function takes exactly one argument. Function called with ' + str(len(sys.argv))
    raise(Exception(error_str))

rootdir_path = sys.argv[1]

if not os.path.isdir(rootdir_path):
    raise('Argument needs to be a directory path')

rootdir_name = os.path.basename(rootdir_path)

contents = ''

contents = list_dir_contents(contents, '')

print '***Contents***'
print contents

