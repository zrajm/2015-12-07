#!/usr/bin/env python

import shutil

def conform(path):
    shutil.copyfile(u'example.mp4', path)
    return path

if __name__ == '__main__':
    conform()
