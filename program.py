#!/usr/bin/env python

import shutil

def conform():
    path = u'/tmp/file.mp4'
    shutil.copyfile(u'example.mp4', path)
    return path

if __name__ == '__main__':
    conform()
