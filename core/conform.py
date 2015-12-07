#!/usr/bin/env python

import shutil, sys, subprocess, os

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
    return (edl_template
        .replace('{{source_file}}', source_file)
        .replace('{{dest_file}}',   dest_file)
    )


def run_dvstory(source_file, dest_file):
    edl = render_edl(
        read_edl_template(),
        os.path.join(os.getcwd(), source_file),
        dest_file,
    )
    edl_file = '/tmp/something.edl'
    with open(edl_file, 'w') as f:
        f.write(edl)
    process = subprocess.Popen(['dvstory-amf', '--input', edl_file])
    return process.wait() == 0

if __name__ == '__main__':
    assert len(sys.argv) == 2, "Exactly one argument/filename required"
    conform(sys.argv[1])
