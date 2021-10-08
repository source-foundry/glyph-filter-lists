#!/usr/bin/env python3

# Copyright 2021 Source Foundry Authors

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import pathlib
import plistlib
import sys


def main(argv):
    glyphs2_plist_inpath = pathlib.Path(
        "~/Library/Application Support/Glyphs/CustomFilter.plist"
    ).expanduser()
    glyphs2_plist_outpath = pathlib.Path("../plist/custom/CustomFilter.plist").resolve()

    try:
        with open(glyphs2_plist_inpath, "rb") as f:
            glyphs2_plist = plistlib.load(f)
    except Exception as e:
        sys.stderr.write(f"Unable to open {glyphs2_plist_inpath}: {e}{os.linesep}")
        sys.exit(1)

    filter_lists = []
    included_filter_names = set()
    custom_filter_text_paths = pathlib.Path("../filters").resolve().glob("*.txt")
    # print(sorted(list(custom_filter_text_paths)))

    for a_list in glyphs2_plist:
        # make Filter obj's from existing default
        filter = Filter(a_list["name"])
        if "list" in a_list:
            filter.list = a_list["list"]
        if "predicate" in a_list:
            filter.predicate = a_list["predicate"]

        filter_lists.append(filter)
        included_filter_names.add(a_list["name"])

    append_filter_lists = []
    for custom_filter_path in sorted(list(custom_filter_text_paths)):
        with open(custom_filter_path) as f:
            filter_definition = f.read()
            filter_name = custom_filter_path.stem
            custom_filter = Filter(filter_name)
            custom_filter.parse_glyph_list(filter_definition)
            if filter_name in included_filter_names:
                # if the filter already exists,
                # overwrite the definition
                for i, a_filter in enumerate(filter_lists):
                    if a_filter.name == filter_name:
                        # remove the old definition from `filter_lists`
                        # it will be appended to the list of filters
                        # in an alphabetized order below
                        del filter_lists[i]
                        append_filter_lists.append(custom_filter)
                        print(f"Updated {filter_name}")
            else:
                # otherwise, write a new filter definition
                append_filter_lists.append(custom_filter)
                included_filter_names.add(filter_name)
                print(f"Added {filter_name}")

    # extend the filter list with *ordered* custom lists
    # using data parsed from this repository
    filter_lists.extend(append_filter_lists)

    # prep the plist
    new_custom_filter_lists = []
    for this_filter in filter_lists:
        new_glyphs_filter = {}
        new_glyphs_filter["name"] = this_filter.name
        if this_filter.predicate:
            new_glyphs_filter["predicate"] = this_filter.predicate
        if len(this_filter.list) > 0:
            new_glyphs_filter["list"] = this_filter.list
        new_custom_filter_lists.append(new_glyphs_filter)

    try:
        with open(glyphs2_plist_outpath, "wb") as f:
            plistlib.dump(new_custom_filter_lists, f, sort_keys=True)
            print(f"{glyphs2_plist_outpath} write complete.")
    except Exception as e:
        sys.stderr.write(f"Error during file write: {e}")
        sys.exit(1)


class Filter(object):
    """Filter is an object that maintains data elements for Glyphs application
    filter lists."""

    def __init__(self, name):
        self.comment_delimiters = ("#", "/")
        self.name = name
        self.predicate = None
        self.list = []

    def __str__(self):
        return (
            f"Filter<name: {self.name}, predicate: {self.predicate}, list: {self.list}>"
        )

    def parse_glyph_list(self, text):
        """Filter class method that defines a Filter object with parsed data
        from newline-delimited text files of list elements"""
        raw_code_point_list = text.splitlines()
        filtered_code_point_list = []
        for item in raw_code_point_list:
            test_item = item.strip()
            if len(test_item) == 0:  # discard blank lines in definition file
                pass
            elif (
                test_item[0] in self.comment_delimiters
            ):  # discard comment lines in definition file
                pass
            else:
                filtered_code_point_list.append(test_item)
        self.list = filtered_code_point_list


if __name__ == "__main__":
    main(sys.argv[1:])
