#!/usr/bin/env python

import shutil

def conform():
    path = u'/tmp/file.mxf'
    shutil.copyfile(u'example.mxf', path)
    return path

if __name__ == '__main__':
    conform()
