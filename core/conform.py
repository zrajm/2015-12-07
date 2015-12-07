#!/usr/bin/env python

from bottle import SimpleTemplate
import shutil, sys

def conform(path):
    run_dvstory(
        source_file = 'example2.mp4',
        dest_file   = path,
    )
    return path

def read_edl_template():
    with open('template.edl', 'r:utf-8') as f:
        return f.read()

def render_edl(edl_template, source_file, dest_file):
    return (read_edl_template()
        .replace('{{source_file}}', source_file)
        .replace('{{dest_file}}',   dest_file)
    )

def run_dvstory(source_file, dest_file):
    shutil.copyfile(source_file, dest_file)
    return dest_file
    

if __name__ == '__main__':
    conform(sys.argv[1])
