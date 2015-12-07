#!/usr/bin/env python

from bottle import SimpleTemplate
import shutil, sys

def conform(path):
    shutil.copyfile(u'example.mp4', path)
    return path

def read_edl_template():
    with open('template.edl', 'r:utf-8') as f:
        return f.read()

def render_edl(edl_template, source_file, dest_file):
    return (read_edl_template()
        .replace('{{source_file}}', source_file)
        .replace('{{dest_file}}',   dest_file)
    )

if __name__ == '__main__':
    conform(sys.argv[1])
