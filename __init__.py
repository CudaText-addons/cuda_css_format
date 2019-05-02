import sys
import os
import json
from cudatext import *
from . import cssbeautifier
from . import cssformatter
from . import format_proc

format_proc.INI = 'cuda_css_format.json'
format_proc.MSG = '[CSS Format] '

formatter = cssformatter.CssFormater()

def options():

    op = cssbeautifier.default_options()
    fn = format_proc.ini_filename()
    if not os.path.isfile(fn):
        return op

    with open(fn) as f:
        d = json.load(f)
        op.indent_size                = d["indent_size"]
        op.indent_char                = d["indent_char"]
        op.selector_separator_newline = d["selector_separator_newline"]
        op.end_with_newline           = d["end_with_newline"]
    return op


def do_format(text):

    return cssbeautifier.beautify(text, options())

def do_format_expand(text):

    return formatter.run(text, 'expand')

def do_format_compact(text):

    return formatter.run(text, 'compact')

def do_format_compress(text):

    return formatter.run(text, 'compress')


class Command:

    def config_global(self):

        format_proc.config_global()

    def config_local(self):

        format_proc.config_local()

    def run(self):

        format_proc.run(do_format)

    def expand(self):

        format_proc.run(do_format_expand)

    def compact(self):

        format_proc.run(do_format_compact)

    def compress(self):

        format_proc.run(do_format_compress)
