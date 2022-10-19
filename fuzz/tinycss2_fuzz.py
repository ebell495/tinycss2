#!/usr/local/bin/python3
import atheris
import sys
import io
import os

with atheris.instrument_imports():
    import tinycss2

@atheris.instrument_func
def TestOneInput(data):
    tinycss2.parse_stylesheet_bytes(data)


atheris.Setup(sys.argv, TestOneInput)
# atheris.instrument_all()
atheris.Fuzz()