#!/usr/bin/env python3

# ==============================================================
#
#
#   glformatter.py
#   Glyph name filter list definition file formatter
#   Copyright 2018 Christopher Simpkins
#   Apache License 2.0
#
#
# ==============================================================

# USAGE
#
# This script is dependent upon the Python 3 interpreter.  If a Python 3 interpreter
# is not available on your system, please see the Python documentation at
# https://www.python.org/downloads/ for instructions on how to install it.
#
#
# Execute the script from any directory on your system by passing one or more
# filepath arguments to local filter list definition files on your system:
#
#    $ python3 glformatter.py [filepath 1] [filepath ...]
#
# The script reformats the text in the filter list definition file with the
# following:
#
#  - adds a comment line above each glyph name definition in the file
#    that includes:
#      - Unicode code point (in hexadecimal name format)
#      - AGL-style nice name (if not used for glyph name definition)
#      - production name (if not used for glyph name definition)
#      - Unicode description
#
# The file write takes place on the original file path. The original file
# is backed up on the path:
#
#     [original file path].pre


import os
import shutil
import sys
import xml.etree.ElementTree as ET

COMMENT_DELIMITERS = ("#", "/")


class Glyph(object):
    def __init__(self):
        self.unicode = ""
        self.name = ""
        self.description = ""
        self.production = ""
        self.alt_names = []


def main(argv):
    glyphlist = []
    unicode_set = set()
    name_set = set()
    production_set = set()
    altname_set = set()

    tree = ET.parse(
        "/Applications/Glyphs.app/Contents/Frameworks/GlyphsCore.framework/Versions/A/Resources/GlyphData.xml"
    )
    root = tree.getroot()
    for child in root:
        glyph = Glyph()
        if "unicode" in child.attrib:
            glyph.unicode = child.attrib["unicode"]
            unicode_set.add(glyph.unicode)
        if "name" in child.attrib:
            glyph.name = child.attrib["name"]
            name_set.add(glyph.name)
        if "description" in child.attrib:
            glyph.description = child.attrib["description"]
        if "production" in child.attrib:
            glyph.production = child.attrib["production"]
            production_set.add(glyph.production)
        if "altNames" in child.attrib:
            namestring = child.attrib["altNames"]
            if len(namestring) > 0:
                name_list = namestring.split(",")
                for altname in name_list:
                    save_name = altname.strip()
                    glyph.alt_names.append(save_name)
                    altname_set.add(save_name)

        glyphlist.append(glyph)

    for filepath in argv:
        if not os.path.isfile(filepath):
            sys.stderr.write(
                "[ERROR] " + filepath + " does not appear to be a valid filepath!"
            )
            sys.exit(1)

        outfile_list = []

        with open(filepath, "r") as f:
            text = f.read()
            text_line_list = text.splitlines()
            for line in text_line_list:
                if line[0] in COMMENT_DELIMITERS:
                    outfile_list.append(line)
                elif len(line) == 0:
                    outfile_list.append("")
                elif line is None:
                    outfile_list.append("")
                else:
                    glyph_name = line
                    if glyph_name in name_set:
                        outfile_list.append(
                            get_comment_string(glyphlist, name=glyph_name)
                        )
                        outfile_list.append(glyph_name + os.linesep)
                    elif glyph_name in production_set:
                        outfile_list.append(
                            get_comment_string(glyphlist, production=glyph_name)
                        )
                        outfile_list.append(glyph_name + os.linesep)
                    else:
                        outfile_list.append(glyph_name + os.linesep)

        # backup file to originalpath with ".pre" suffix
        backup_filepath = filepath + ".pre"
        shutil.copyfile(filepath, backup_filepath)

        # write out formatted file
        out_text = "\n".join(outfile_list)
        with open(filepath, "w") as f:
            f.write(out_text)


def get_comment_string(glyphlist, name=None, production=None):
    if name is not None:
        for glyph in glyphlist:
            if glyph.name == name:
                comment_string = "# "
                if len(glyph.unicode) > 0:
                    comment_string += "U+" + glyph.unicode
                if len(glyph.production) > 0:
                    comment_string += " | " + glyph.production
                if len(glyph.description) > 0:
                    comment_string += " | " + glyph.description
                return comment_string
    elif production is not None:
        for glyph in glyphlist:
            if glyph.production == production:
                comment_string = "# "
                if len(glyph.unicode) > 0:
                    comment_string += "U+" + glyph.unicode
                if len(glyph.name) > 0:
                    comment_string += " | " + glyph.name
                if len(glyph.description) > 0:
                    comment_string += " | " + glyph.description
                return comment_string
    else:
        return ""


if __name__ == "__main__":
    main(sys.argv[1:])
