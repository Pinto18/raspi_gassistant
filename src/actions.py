#!/usr/bin/env python

import subprocess

def shutdown():
    subprocess.call(
        ["sudo",
         "shutdown",
         "-h",
         "now"]
    )