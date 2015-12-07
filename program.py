#!/usr/bin/env python

def conform():
    path = u'/tmp/file.mxf'

    with open(path, 'w') as f:
        f.write('hello world')

    return path
