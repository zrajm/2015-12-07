#!/usr/bin/env python

from bottle import SimpleTemplate
import shutil, sys


def conform(path):
    shutil.copyfile(u'example.mp4', path)
    return path

if __name__ == '__main__':
    conform(sys.argv[1])
